import sys
import numpy as np
import random
import multiprocessing as mp

if len(sys.argv) != 7:
    print("This is a sample code from my PhD I developed for a simple system.")
    print("It can evaluate the excess chemical potential of various solutes in solvent.")
    print("usage:Python TPI.py numWater Temperature numInsertion sigma_aw epsilon_aw cutoff < out.gro")
    print("number of water is integer, Temperature is K, numInsertion is integer, sigma_aw is the sigma of solute-solvent and is in Angstrom,")
    print("epsilon_aw is K, and it is between solute-solvent. cutoff is in Angstrom")
    sys.exit()



numwater = int(sys.argv[1])
T = float(sys.argv[2])
R = 8.31446261815324 * 0.001  # kJ/mol.K
betta = 1 / (R * T) 
Ninsertion = int(sys.argv[3])
sigma = float(sys.argv[4]) * 0.1  # nm
epsilon = float(sys.argv[5]) * R  # Confirm this value against literature
rc = float(sys.argv[6]) * 0.1  # Standard cutoff


c6 = 4.0 * epsilon * sigma**6
c12 = 4.0 * epsilon * sigma**12
ri6 = 1.0 / (rc**6)
ri3 = 1.0 / (rc**3)

tail_factor = (4.0/3.0) * np.pi * ri3 * (1.0/3.0 * c12 * ri6 - c6)
x, y, z, lx, ly, lz = [], [], [], [], [], []
for line in sys.stdin:
    p = line.split()
    if len(p) == 6:
        x.append(float(p[3]))
        y.append(float(p[4]))
        z.append(float(p[5]))
    elif len(p) == 3:
        lx.append(float(p[0]))
        ly.append(float(p[1]))
        lz.append(float(p[2]))


numframes = len(x) // numwater 

def FandE_virtual(args):
    
    x_test, y_test, z_test, X1, Y1, Z1, Lx, Ly, Lz, rc, sigma, epsilon = args 
    V = Lx * Ly * Lz
    n = numwater
    rc2 = rc ** 2
    en = 0.0

    for i in range(numwater):
        dx = X1[i] - x_test
        dy = Y1[i] - y_test
        dz = Z1[i] - z_test

        dx -= Lx * round(dx / Lx)
        dy -= Ly * round(dy / Ly)
        dz -= Lz * round(dz / Lz)

        r2 = dx ** 2 + dy ** 2 + dz ** 2
        if r2 < rc2:
            r = np.sqrt(r2)
            PE = 4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)
            en += PE 

    return en 



def process_frame(frame_idx):
    wtest = 0
    X1 = x[frame_idx*numwater:frame_idx*numwater+numwater]
    Y1 = y[frame_idx*numwater:frame_idx*numwater+numwater]
    Z1 = z[frame_idx*numwater:frame_idx*numwater+numwater] 
    Lx = lx[frame_idx]
    Ly = ly[frame_idx]
    Lz = lz[frame_idx] 
        
    V = (Lx * Ly * Lz)
    
    inputs = [
        (Lx * random.random(), Ly * random.random(), Lz * random.random(), X1, Y1, Z1, Lx, Ly, Lz, rc, sigma, epsilon)
        for _ in range(Ninsertion)
    ]
    
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(FandE_virtual, inputs)
    
    pe = [i + (numwater / V) * tail_factor for i in results]
    for test_particle_energy in pe:
        wtest += np.exp(-betta * test_particle_energy)

    PE = (wtest * V) / Ninsertion
    
    
    
    return PE

if __name__ == "__main__":
    data_PE = []    
    for i in range(int(numframes)):
        data_PE.append(process_frame(i))
        
    data_PE = data_PE[1:]
    data_V = []
    for i in range(len(lx)):
        data_V.append(lx[i] * ly[i] * lz[i])

    data_V = data_V[1:]
    numBlock = 5
    block_size = len(data_V) // 5
    data_log = []
    for i in range(numBlock):
        v = np.sum(data_V[i*block_size:block_size*i+block_size])/len(data_V[i*block_size:block_size*i+block_size])
        pe = np.sum(data_PE[i*block_size:block_size*i+block_size])/len(data_PE[i*block_size:block_size*i+block_size])
        data_log.append(- (1 / betta) * np.log(pe/v))
    error = np.std(data_log)/np.sqrt(numBlock)
    print(str(np.mean(data_log)) + " +/- " + str(error) + " kj/mol") 



