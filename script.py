import os, re, sys

# Set the directory path where your files are stored
directory = r'C:/Users/KRAKENDEVDocuments/git/test'

# Set the file data type (eg. .png, .jpg, .jpeg)
dataType = ".txt"

# Validate directory
try:
    file_list = os.listdir(directory)
except FileNotFoundError:
    print("Directory folder not found or not valid!")
    print("Current directory: " + directory)
    sys.exit()

# Get the list of file names in the directory
file_list = os.listdir(directory)

# Sort the file names in ascending order using natural sorting
def natural_sort_key(s):
    return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', s)]
file_list.sort(key=natural_sort_key)

# Initialize the counter to 0
counter = 0

# Loop through all files in the directory
for filename in file_list:
    # Check if the file is a image file
    if filename.endswith(dataType):
        # Construct the new filename with the counter and file extension
        new_filename = str(counter) + dataType
        # Construct the full path for the old and new file names
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        # Check if the new file name already exists
        while os.path.exists(new_filepath):
            # If it does, append a number to the end of the file name
            counter += 1
            new_filename = str(counter) + dataType
            new_filepath = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_filepath, new_filepath)
        # Increment the counter
        counter += 1
    print(filename + " -> " + new_filename)
