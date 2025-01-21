import shutil, os

# Specify folder and file name for the first folder
folder1 = 'touhid/'
file_path1 = folder1 + 'example.txt'

# Create the folder if it doesn't exist
os.makedirs(folder1, exist_ok=True)

# Create the file in folder1 and write text to it
open(file_path1, 'w') 
    

# Specify folder and file name for the second folder
folder2 = 'touhid1/'

# Create folder2 if it doesn't exist
os.makedirs(folder2, exist_ok=True)

# Create the file in folder2 and write text to it (optional, can skip if only copying)


# Define the source file and the target directory for copying
source_file = 'touhid/example.txt'
destination_dir = 'touhid1/'

# Copy the file to the destination directory
shutil.copy(source_file, destination_dir)

print("File copied successfully!")
