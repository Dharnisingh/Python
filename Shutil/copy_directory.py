# Program to copy the directory

import os
import shutil

src = "/home/dharni/Python/Shutil/src"
dest = "/home/dharni/Python/Shutil/dest1/"

shutil.copytree(src,dest)
print(os.listdir(dest))
