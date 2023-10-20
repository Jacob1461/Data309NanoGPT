#!/bin/bash
#SBATCH --job-name=train_and_sample
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:3
#SBATCH --exclusive


cd out
rm ckpt.pt
cd ..

python3 train.py config/gpt3-small-like32batch128block.py  --device='cuda' --compile=True

if [ $? -eq 0 ]; then
  python3 sample.py --device='cuda' --compile=True 
else
  echo "Did not run because the train ran into an error"
fi 	
