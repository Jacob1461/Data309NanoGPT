import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
input_filename = 'lyric_samples.txt'
output_base = 'sample'
output_folder = 'samples'  # New folder name

current_output_file = None
output_count = 1
lines_to_skip = 4  # Skip the preamble that the samples make at the top


if not os.path.exists(output_folder):
    os.mkdir(output_folder)

with open(input_filename, 'r') as infile:
    lines_before_separator = []  # To store lines before the first "---------------"
    
    for line_number, line in enumerate(infile, start=1):
        if line_number <= lines_to_skip:
            continue
        
        if line.strip() == '---------------':
            if current_output_file is None:
                # If no output file is open, create sample1.txt and write lines before the first "---------------"
                output_filename = os.path.join(output_folder, f'{output_base}{output_count}.txt')
                current_output_file = open(output_filename, 'w')
                current_output_file.writelines(lines_before_separator)
                output_count += 1
            elif lines_before_separator:  # Only close if there are lines to write
                current_output_file.close()
            output_filename = os.path.join(output_folder, f'{output_base}{output_count}.txt')
            current_output_file = open(output_filename, 'w')
            output_count += 1
            lines_before_separator = [] 
        elif current_output_file:
            current_output_file.write(line)
        else:
            lines_before_separator.append(line)

if current_output_file and lines_before_separator: 
    current_output_file.close()
