import os
import shutil

# Set the source and destination folders
src_folder = "C:/Users/Username/Downloads"
dst_folder = "C:/Users/Username/Documents/PDFs"

# Create the destination folder if it doesn't already exist
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

# Loop through all files in the source folder
for filename in os.listdir(src_folder):
    # Check if the file has a .pdf extension
    if filename.endswith(".pdf"):
        # Construct the full path to the source and destination files
        src_file = os.path.join(src_folder, filename)
        dst_file = os.path.join(dst_folder, filename)
        # Move the file to the destination folder
        shutil.move(src_file, dst_file)
        print(f"Moved {filename} to {dst_folder}")
