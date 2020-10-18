#!/bin/bash

#SBATCH --mail-user=ykent@iastate.edu 
#SBATCH --mail-type=end
#SBATCH --partition=normal
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --job-name=MnO-VV

# record start date and host
date
hostname

work_dir=${PWD}
mkdir -p /tmp/ykent$SLURM_JOB_ID
cp * /tmp/ykent$SLURM_JOB_ID
cd /tmp/ykent$SLURM_JOB_ID
mpirun -np 8 /home/ykent/GitLab/comrisb/bin/rspflapw.exe 
cp * ${work_dir}
cd ..
rm -r /tmp/ykent$SLURM_JOB_ID

# record end date
date

