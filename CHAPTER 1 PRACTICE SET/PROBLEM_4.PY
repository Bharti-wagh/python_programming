#TASK : write a python program to print contents of directory using the os module. search online for the function which does that.
#TASK : LABEL THE CODE
import os

# Get the current working directory
current_directory = os.getcwd()

print(f"Contents of directory: {current_directory}")
print("-" * 40)

# List all files and directories
contents = os.listdir(current_directory)

# Print each item
for item in contents:
    print(item)
