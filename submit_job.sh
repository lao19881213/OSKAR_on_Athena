#!/bin/bash 
#SBATCH --nodes=1
#SBATCH --partition=gpuq
#SBATCH --gres=gpu:1
#SBATCH --time=00:10:00
#SBATCH --account=pawsey0245

source /home/blao/OSKAR/bashrc


srun -n 1 python run.py sim_gleam.json
