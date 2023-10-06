input_filename = '~/jacobstuff/nanoGPT-master/output_config/bigtrain2py.txt'
output_base = 'sample'

# Initialize variables
current_output_file = None
output_count = 1
lines_to_skip = 3  # Number of lines to skip at the beginning

# Open the input file for reading
with open(input_filename, 'r') as infile:
    lines_before_separator = []  # To store lines before the first "---------------"
    
    for line_number, line in enumerate(infile, start=1):
        if line_number <= lines_to_skip:
            # Skip the first 'lines_to_skip' lines
            continue
        
        if line.strip() == '---------------':
            if current_output_file is None:
                # If no output file is open, create sample1.txt and write lines before the first "---------------"
                output_filename = f'{output_base}{output_count}.txt'
                current_output_file = open(output_filename, 'w')
                current_output_file.writelines(lines_before_separator)
                output_count += 1
            # Close the current output file (if it's open)
            if current_output_file:
                current_output_file.close()
            # Open the next output file
            output_filename = f'{output_base}{output_count}.txt'
            current_output_file = open(output_filename, 'w')
            output_count += 1
            lines_before_separator = []  # Reset lines_before_separator
        elif current_output_file:
            # Write the line to the current output file
            current_output_file.write(line)
        else:
            # Store lines before the first "---------------" in lines_before_separator
            lines_before_separator.append(line)

# Close the last output file (if it's open)
if current_output_file:
    current_output_file.close()
