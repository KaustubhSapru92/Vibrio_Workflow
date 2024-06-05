import os
import shutil
import sys

# Get the directory where the script is located
source_directory = os.path.dirname(os.path.abspath(__file__))

# Ensure that a new folder name is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python script.py <new_folder_name>")
    sys.exit(1)

# Get the new folder name from the argument
new_folder_name = sys.argv[1]

# Define the target directory based on the new folder name
target_directory = os.path.join(source_directory, new_folder_name)

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Get a list of all .fa files in the source directory that contain 'S129'
fa_files = [f for f in os.listdir(source_directory) if f.endswith('.fa') and 'SRR129' in f]

# Copy each .fa file to the target directory
for file in fa_files:
    source_file_path = os.path.join(source_directory, file)
    target_file_path = os.path.join(target_directory, file)
    shutil.copy(source_file_path, target_file_path)
    print(f"Copied {file} to {target_directory}")

print("All .fa files have been copied successfully.")

