import cv2
import os
import shutil
import sys

# Get the value of n from the command line (default to 999)
n = int(sys.argv[1]) if len(sys.argv) > 1 else 777
print_output = True if len(sys.argv) <= 1 else False

# Create the "contours" subdirectory if it doesn't exist
if not os.path.exists("contours"):
    os.mkdir("contours")

def detect_image_type(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            if print_output:
                print(f"Error: Failed to read {image_path}")
            return
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 200)
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if print_output:
            print(f"{image_path} has {len(contours)} contours.")
        if len(contours) > n:
            shutil.move(image_path, os.path.join("contours", os.path.basename(image_path)))
    except cv2.error as e:
        if print_output:
            print(f"Error processing {image_path}: {str(e)}")

for filename in os.listdir("."):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(".", filename)
        detect_image_type(image_path)

        
        
'''
This script performs the following tasks:

Imports necessary libraries: cv2 for image processing, os for operating system-related functions, shutil for file operations, and sys for command line arguments.

Reads the value of n from the command line argument (defaulting to 777 if not provided). It also checks if the print_output flag is set based on the command line argument.

Creates a subdirectory named "contours" if it doesn't already exist.

Defines a function detect_image_type(image_path) which takes an image path as input and performs the following steps:

Reads the image using cv2.imread.
Checks if the image is valid. If not, it prints an error message (if print_output is set) and returns.
Converts the image to grayscale using cv2.cvtColor.
Applies Gaussian blur to the grayscale image using cv2.GaussianBlur.
Detects edges in the blurred image using the Canny edge detection algorithm with specified thresholds.
Finds contours in the edge image using cv2.findContours.
Prints the number of contours (if print_output is set).
If the number of contours is greater than n, it moves the image to the "contours" subdirectory using shutil.move.
Iterates through all files in the current directory using os.listdir(".").

For each file with a ".jpg" or ".png" extension, it constructs the image path and calls the detect_image_type function.
The script essentially detects the number of contours in each image file (JPEG or PNG) in the current directory. If the number of contours exceeds the specified threshold n, it moves the image to a subdirectory called "contours". The print_output flag determines whether or not to print the number of contours for each image.


'''        
