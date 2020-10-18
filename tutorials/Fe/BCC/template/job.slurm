#!/bin/bash

#SBATCH --mail-user=ykent@iastate.edu 
#SBATCH --mail-type=end
#SBATCH --partition=normal
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --job-name=Fe-VV

# record start date and host
date
hostname

mpirun -np 8 /home/ykent/GitLab/comrisb/bin/rspflapw.exe 

# record end date
date

