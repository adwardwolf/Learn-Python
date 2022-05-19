import os
import time
import shutil

# File detection

path = "poetry.txt"
dir_path = "poetry"

if os.path.exists(dir_path):
    print("That location exists")
    if os.path.isdir(dir_path):
        print("That is a directory")
    elif os.path.isfile(dir_path):
        print("That is a file")
else:
    print("That file does not exist!")

# Read file

try:
    with open("poetry.txt") as file:
        text = file.read()
        for i in text:
            print(i, end="")
            time.sleep(0.005)
except FileNotFoundError:
    print("File was not found :(")

# Write file

text = "\nI love it"

# Replace text in the file
with open("poetry.txt", 'w') as file:
    file.write(text)

# Append text to the file
with open("poetry.txt", 'a') as file:
    file.write(text)

# Copy File

shutil.copyfile('poetry.txt', 'poetry_copy.txt')

# Move File

source = "poetry.txt"
destination = "poetry/poetry.txt"

try:
    if os.path.exists(destination):
        print("File in that destination is already exist!")
    else:
        os.replace(source, destination)
        print(source, "has been moved")
except FileNotFoundError:
    print("File not found!")

# Delete file

try:
    os.remove('poetry.txt')  # remove file
    os.rmdir('poetry')  # remove directory
    shutil.rmtree('poetry')  # be careful, this function will delete a directory and everything inside
except FileNotFoundError:
    print("That file was not found!")
except OSError:
    print("You cannot delete non-empty directory with rmdir function!")
else:
    print("Item has been deleted!")
