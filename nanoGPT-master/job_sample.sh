#!/bin/bash
#SBATCH --job-name=increase4testtrain
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:2
#SBATCH --exclusive

python3 sample.py --device='cuda' 
