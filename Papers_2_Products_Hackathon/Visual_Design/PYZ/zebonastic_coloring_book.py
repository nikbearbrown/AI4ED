import os
import subprocess

input_dir = os.getcwd()  # Current working directory
output_dir = os.getcwd()  # Current working directory

for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        input_path = os.path.join(input_dir, filename)
        file_name, file_extension = os.path.splitext(filename)
        output_filename = file_name + "_cbook" + file_extension
        output_path = os.path.join(output_dir, output_filename)

        # ImageMagick command to convert the image
        command = f'convert "{input_path}" -colorspace gray -edge 1 -negate "{output_path}"'
        command = f'convert "{input_path}" -colorspace gray -edge 1 "{output_path}"'
        command = f'convert "{input_path}" -edge 3 "{output_path}"'  
        command = f'convert "{input_path}" -colorspace gray "{output_path}"'              
        # Execute the command
        subprocess.run(command, shell=True)
        
'''
This script performs image processing tasks on PNG files using the ImageMagick command-line tool. Here's a breakdown of what the script does:

It imports the necessary modules, os and subprocess, which are used for interacting with the operating system and executing shell commands, respectively.

The current working directory is obtained using os.getcwd() and assigned to both input_dir and output_dir variables. This means that the script will look for PNG files in the current directory and save the processed images in the same directory.

The script iterates over the files in the input_dir using os.listdir(input_dir).

For each file, it checks if the file name ends with ".png" using filename.endswith(".png").

If the file is a PNG file, it creates the input and output paths using os.path.join() to concatenate the directory path with the file name.

It extracts the file name and extension using os.path.splitext(filename).

It constructs the output file name by appending "_cbook" before the file extension.

It constructs an ImageMagick command to perform image processing operations on the input image. There are multiple variations of the command shown in the script, commented out with #. You can choose which one to use by uncommenting the desired line or modifying them as per your requirements. Here's an explanation of the options used in the commands:

-colorspace gray: Converts the image to grayscale.
-edge 1 or -edge 3: Applies edge detection to the image, creating a line drawing effect. The value represents the radius of the area used for edge detection.
-negate: Inverts the colors of the image.
Depending on the desired effect, you can select and modify the command accordingly.

After constructing the ImageMagick command, it uses subprocess.run() to execute the command in the shell. The shell=True argument is set to allow the use of shell-specific features like command chaining and redirection.

By running this script, it will process all PNG files in the current directory using the selected ImageMagick command and save the resulting images with the "_cbook" suffix in the same directory.

'''        

