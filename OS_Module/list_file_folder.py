# List all files and folder inside of specified folder
import os

for root, folders, files in os.walk("/home/dharni/pyhon"):
    print("Root folder:\n",root)
    print("List of folders:")
    for i in folders:
        print(os.path.join(root,i))

    print("List of files:\n",files)
