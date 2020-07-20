print("This program will create a new file and write some content to tat\n")

with open("/home/new_fil",'w+') as f:
    f.writelines("Hello this is new file\n")
    f.writelines("How are you doing\n")
    f.writelines("Lets see how it goes")

print("Writing is done")
