# Operation on directory using OS module

import os
# Get the current working direcctory as string
cwd = os.getcwd()
print("Current working directory: ", cwd)

# Change directory returns None
os.chdir('../String')
print("After chdir: ", os.getcwd())

# List the contents of directory
# returns list of directory contents
ret = os.listdir(os.getcwd())
print("Contents of directory: ",ret)

# Make directory 
# makdir() method just create one directory
# Recursively create directory and return None
if(not os.path.isdir('dir1/dir2/dir3')):
    # Check if directory already does not exist before creating
    os.makedirs('dir1/dir2/dir3')

# Remove directory
# rmdirs() remove diectory recursively
# Check before removin if directroy already exist
# if directory does not exist you will get error FileNotFoud 
if(os.path.isdir('dir1/dir2/dir3')):
    os.removedirs('dir1/dir2/dir3')

# Traverse the directory
# return tuple of ther objects root, directory, files
for root, dirs , files  in os.walk('.'):
    for name in files:
        print(name)
    for name in dirs:
        print(name)
    print("Root: ", root)

# Check if a file exists
# Returns True or False
ret = os.path.exists("find_str.py")
if(ret == True):
    print("File exist")
