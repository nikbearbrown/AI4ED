import sys
import os
import csv
import random


def extract_text_before_double_dashes(line):
    end_index = line.find('--')

    if end_index != -1:
        return line[:end_index].strip()
    else:
        return line.strip()


def extract_text_between_asterisks(line):
    start_index = line.find('**')
    end_index = line.find('**', start_index + 2)

    if start_index != -1 and end_index != -1:
        return line[start_index + 2: end_index].strip()
    else:
        return line.strip()


def cleanup_string(input_string):
    # Replace ** with a space
    cleaned_string = re.sub(r'\*\*', ' ', input_string)

    # Replace "Upscaled by", "Variations by", and "Upscaled (Light) by" with a space
    cleaned_string = re.sub(r'Upscaled by|Variations by|Upscaled \(Light\) by', ' ', cleaned_string)

    # Replace -- with a space
    cleaned_string = re.sub(r'--', ' ', cleaned_string)

    # Replace - white space - with a space
    cleaned_string = re.sub(r'-\s-\s-', ' ', cleaned_string)

    # Remove single digits or characters with whitespace before and after
    cleaned_string = re.sub(r'\s\w\s|\b\w\b', ' ', cleaned_string)

    # Replace multiple whitespace with a single space
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string)

    # Remove leading and trailing whitespace
    cleaned_string = cleaned_string.strip()

    return cleaned_string


def clean_csv_file(input_file):
    # Create a list to store unique lines
    unique_lines = []

    # Open the input file for reading
    with open(input_file, 'r') as f:
        # Read each line from the file
        for line in f:
            # Replace tabs with commas if the line contains tabs
            if '\t' in line:
                line = line.replace('\t', ',')

            # Remove the word "IMAGE" and leading/trailing quotes
            line = line.replace('IMAGE', '').strip('"\'')
            # Remove carriage returns and leading/trailing white space
            line = line.replace('\r', '').strip()
            # Remove double quotes at the end of the line
            if line.endswith('"'):
                line = line[:-1]
            # Remove lines shorter than 44 characters
            if len(line) >= 44:
                # Add the line to the list of unique lines
                unique_lines.append(line)

    # Shuffle the list of unique lines
    random.shuffle(unique_lines)

    # Create a new file name for the output file
    output_file = input_file.replace('.', '_clean.')

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Write each unique line to the output file
        for line in unique_lines:
            # Remove leading/trailing white space and write to file
            f.write(line.strip() + '\n')

    print(f"CSV file cleaned and saved as {output_file} successfully.")


def merge_and_clean_csv_files(output_file_name):
    # Get a list of all CSV files in the current directory
    csv_files = [file for file in os.listdir(".") if file.endswith(".csv")]

    if not csv_files:
        print("No CSV files found in the current directory.")
        return

    # Sort the CSV files alphabetically
    csv_files.sort()

    # Create the output file name
    output_file = output_file_name if output_file_name else "prompts_clean.csv"

    # Create a list to store unique lines
    unique_lines = []

    # Merge and clean the data from all CSV files
    for csv_file in csv_files:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)

            for row in reader:
                line = ', '.join(row)

                # Replace tabs with commas if the line contains tabs
                if '\t' in line:
                    line = line.replace('\t', ',')

                line = line.rstrip(',')
                line = extract_text_before_double_dashes(line)
                line = extract_text_between_asterisks(line)                
                
                               
                # Remove lines shorter than 44 characters
                if len(line) >= 44:
                    # Add the line to the list of unique lines
                    unique_lines.append(line)

    # Shuffle the list of unique lines
    unique_lines = list(set(unique_lines))    
    random.shuffle(unique_lines)

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Write each unique line to the output file
        for line in unique_lines:
            # Remove leading/trailing white space and write to file
            f.write(line.strip() + '\n')

    print(f"CSV files merged and cleaned. Output file: {output_file}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        clean_csv_file(input_file)
    else:
        output_name = sys.argv[2] if len(sys.argv) > 2 else None
        merge_and_clean_csv_files(output_name)
        
        
'''

This script performs various operations on CSV files.

Here's a breakdown of what the script does:

Imports necessary modules: sys, os, csv, and random.

Defines several helper functions:

extract_text_before_double_dashes(line): Extracts the text before double dashes (--) in a line.
extract_text_between_asterisks(line): Extracts the text between double asterisks (**) in a line.
cleanup_string(input_string): Performs various cleaning operations on a string.
clean_csv_file(input_file): Cleans a CSV file by removing unnecessary characters and lines.
merge_and_clean_csv_files(output_file_name): Merges and cleans multiple CSV files.
Checks if the script is being executed directly and not imported as a module.

If command-line arguments are provided:

If only one argument is provided, it assumes it is the input file and calls the clean_csv_file function on it.
If more than one argument is provided, it assumes the second argument is the output file name and calls the merge_and_clean_csv_files function.
The script reads CSV files, performs cleaning operations on the data, removes unnecessary lines and characters, shuffles the lines, and writes the cleaned data to output files.

Note that the script assumes the CSV files are located in the current directory where the script is executed.

'''        
