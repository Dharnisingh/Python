# program to implement movement of file cursor

with open("file.txt", 'r+') as f:
    # Traverse file by line
    for line in f:
        print("line: {}".format(line, ), end="")

    # Go to end of File
    # 0: begin
    # 1: current
    # 2: end 
    f.seek(2)
    print(f.tell())
    f.write("I am end of the file\n")
    
    f.seek(f.tell(), 0) # second arg whence should be 0,1, or 2
    print("Positin: ", f.tell())

    f.seek(20) # move 20 bytes from begin
    print("Positin: ", f.tell())
