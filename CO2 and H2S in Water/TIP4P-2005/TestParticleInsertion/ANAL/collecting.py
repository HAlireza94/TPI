import numpy as np

mio_CO2, er_CO2, mio_H2S, er_H2S = [], [], [], []
for i in range(11):
	with open('Results-t'+str(i)) as f:
		for line in f:
			p = line.split()
			if len(p) == 5:
				if p[0] == 'CO2':
					mio_CO2.append(float(p[1]))
					er_CO2.append(float(p[3]))
				elif p[0] == 'H2S':
					mio_H2S.append(float(p[1]))
					er_H2S.append(float(p[3]))



temp = np.linspace(270,370,11)

print(mio_CO2)
#for i in range(len(mio_CO2)):
#	print(f"{temp[i]:<10}{mio_CO2[i]:<10.4f}{er_CO2[i]:<10.4f}")


