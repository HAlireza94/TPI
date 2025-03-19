#!/bin/bash
#SBATCH --qos=normal
#SBATCH --job-name=T5                          # Job Name
#SBATCH -o LOG_eq                                   # Log file
#SBATCH --time=24:00:00                             # WallTime
#SBATCH --nodes=1                                   # Number of Nodes
#SBATCH --mem=64000

#SBATCH --ntasks-per-node=1                         # Number of tasks (MPI presseces)
#SBATCH --cpus-per-task=20                          # Number of processors per task OpenMP threads()
#SBATCH --gres=mic:0                                # Number of Co-Processors
#SBATCH --mail-type=ALL                             # Add all jobs to the the mailing list
#SBATCH --mail-user=ahosseini@tulane.edu            # Send notification to the address when job begins and ends


date
module load gcc/6.3.0
module load gromacs/2020.7
## export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
## Production_HR (333K)

time 
set -e









gmx grompp -f mdp/eql-t5.mdp -o eql-t5 -po eql-t5 -pp eql-t5 -c min -t min -maxwarn 1
gmx mdrun -deffnm eql-t5
gmx grompp -f mdp/prd-t5.mdp -o prd-t5 -po prd-t5 -pp prd-t5 -c eql-t5 -t eql-t5
gmx mdrun -deffnm prd-t5
