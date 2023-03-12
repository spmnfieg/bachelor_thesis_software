#!/bin/bash

#SBATCH -J My_first_job
#SBATCH -N 1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=24

# runtime after which the job will be killed (estimated)
#SBATCH -t 02:00:00
# Change to the directory the job was submitted from
cd $SLURM_SUBMIT_DIR

python3 scratch_predict.py