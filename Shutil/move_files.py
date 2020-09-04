# Python program to explain shutil.move() method  
      
# importing os module  
import os  
  
# importing shutil module  
import shutil  
  
# path  
path = '/home/dharni/Python/Shutil'
  
# List files and directories  
# in '/home/dharni/Python/Shutil'  
print("Before moving file:")  
print(os.listdir(path))  
  
# Source path  
source = '/home/dharni/Python/Shutil/src'
  
# Destination path  
destination = '/home/dharni/Python/Shutil/dest'
  
# Move the content of source to destination recurcively
# If the destination is an existing directory, then src is moved inside that directory
dest = shutil.move(source, destination)  
  
# List files and directories  
# in "/home/dharni/Python/Shutil"  
print("After moving file:")  
print(os.listdir(path))  
  
# Print path of newly  
# created file  
print("Destination path:", dest)  

