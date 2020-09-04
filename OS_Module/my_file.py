# Perform operation on file objects using OS module
import os
# Get a file path from home directory
file_path = os.path.join(os.environ.get('HOME'),"FILE_NAME")
print(file_path)

# Geth file/directory anme from specified path
#file_path = os.path.basename('directory_operation.py')
file_path = os.path.basename('/home/dharni')
print("Path of file: ", file_path)

# Check if a path exists
ret = os.path.exists("/home/dharni/abd")
print("Paht: ",ret)

# Returns path of Directory where file is present
ret = os.path.dirname("/home/dharni/test.txt")
print("Directory path: ", ret)

# Return list of directory
ret = os.path.split("/home/dharni/Python")
for i in ret:
    print(i)
# Create a file
ret = os.path.isfile('test.txt')
if not ret:
    os.mknod('test.txt')
    print('File Created: ')

# Rename the file
ret = os.path.exists("test.txt")
if ret:
    os.rename('test.txt', 'new_file.txt')
    print("File renamed")

# Remove the file
ret = os.path.exists("new_file.txt")
if ret:
    os.remove('new_file.txt')
    print("File removed")

# Properties of file
prop = os.stat('file_operation.py')
print(prop)
print("Modified time: ", prop.st_mtime)
