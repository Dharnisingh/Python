# Basic read write and open close operation

# Create a file with write mode
# It will overwrite the the file
with open("temp.txt", 'w') as f:
    # Pritnt the file name
    print("Created file: ", f.name)
    print("Mode: ", f.mode)
    print("File Descriptor: ",f.fileno())

    # Writing Data to file
    f.write("Hello this is first line\n")
    f.writelines("This is the second line\n")
    f.write("Last line\n")
# Reading from file
with open("temp.txt",'r') as f:
    # To read line by line
    for line in f:
        # if end keyword is not given in print it will print one extr line
        print(line, end="")
