# Program to reverse string

st = "GreatGod"
print(st[::-1])

#using reversed() method
# reversed() method returns a reversed object
rev = reversed(st)
for i in rev:
    print(i,end="")
print("")
