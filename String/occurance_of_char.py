# Find occurence of characters in a given string

text = "Find occurence of each character in this string"

#text = text.replace(' ','')
# OR
text = "".join(text)
d = dict()

for c in text:
    d[c] = text.count(c)
print(d.items())
