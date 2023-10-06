#!/bin/bash

# Define a list of parameter configurations
configs=(
    "config/increase1.py"
    "config/increase2.py"
    "config/increase3.py"
    "config/increase4.py"
    "config/increase5.py")

# Loop through each configuration
for config in "${configs[@]}"; do
    echo "Training with config: $config"
    python3 train.py "$config" 

    echo "Sampling with config: $config"
    python3 sample.py --device=cuda > "output_${config}.txt"  # Save output to a file
done

echo "Training and sampling completed for all configurations"
