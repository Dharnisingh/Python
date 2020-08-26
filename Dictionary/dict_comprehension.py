# Dictionary Comprehension

# Using zip method
# zip() takes two iterable sequence and returs a tuple

key = ['d','c','a','b']
val = [1,2,3,4]

d = dict(zip(key,val))
print(d)

d = {k:v for (k,v) in zip(key,val)} 
print(d)

d = {key:key*key for key in range(1,10) }
print(d)
