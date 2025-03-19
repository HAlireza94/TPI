#!/bin/bash
#SBATCH --qos=normal
#SBATCH --job-name=T7                                # Job Name
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








module load anaconda3/5.1.0
./config
