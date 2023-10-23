input_filename = '~/jacobstuff/nanoGPT-master/output_config/bigtrain2py.txt'
output_base = 'sample'


current_output_file = None
output_count = 1
lines_to_skip = 3 #Skip the preamble that the samples make at the top

with open(input_filename, 'r') as infile:
    lines_before_separator = []  # To store lines before the first "---------------"
    
    for line_number, line in enumerate(infile, start=1):
        if line_number <= lines_to_skip:
            continue
        
        if line.strip() == '---------------':
            if current_output_file is None:
                # If no output file is open, create sample1.txt and write lines before the first "---------------"
                output_filename = f'{output_base}{output_count}.txt'
                current_output_file = open(output_filename, 'w')
                current_output_file.writelines(lines_before_separator)
                output_count += 1
            if current_output_file:
                current_output_file.close()
            output_filename = f'{output_base}{output_count}.txt'
            current_output_file = open(output_filename, 'w')
            output_count += 1
            lines_before_separator = []  # Reset lines_before_separator
        elif current_output_file:
            current_output_file.write(line)
        else:
            lines_before_separator.append(line)

if current_output_file:
    current_output_file.close()
