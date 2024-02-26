import os
import random
import string
from pathlib import Path
import sys

def alpha_numeric(n):
    non_ascii_letters = ''.join([char for char in string.printable if char not in string.ascii_letters and ord(char) < 128 and char.isprintable()])
    alpha_numeric = string.ascii_letters + string.digits
    result = ''
    while len(result) < n:
        result += random.choice(alpha_numeric)
    result += str(random.randint(0, 9))
    return result

# Get the current directory name
current_directory = os.getcwd()

# Get the provided group_id from command line
if len(sys.argv) < 2:
    print("Please provide the group_id as a command line argument.")
    sys.exit(1)

group_id = sys.argv[1]

# Get a list of PNG files in the current directory
png_files = [file for file in os.listdir('.') if file.lower().endswith('.png')]

# Rename each PNG file
for filename in png_files:
    file_parts = os.path.splitext(filename)
    image_id = alpha_numeric(5)
    if 'topaz' in filename.lower():
        new_filename = f"topaz_{group_id}_{image_id}.png"
    else:
        new_filename = f"mj_{group_id}_{image_id}.png"
    os.rename(filename, new_filename)

print("PNG files have been renamed.")

