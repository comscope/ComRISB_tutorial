#!/bin/bash

#SBATCH --mail-user=ykent@iastate.edu 
#SBATCH --mail-type=end
#SBATCH --partition=normal
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --job-name=Fe

# record start date and host
date
hostname

/home/ykent/GitLab/comrisb/bin/comrisb.py -c >& log 

# record end date
date

