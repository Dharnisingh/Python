# Strip characters from begining and the end of a given string

text = "aRemove null from begining and enda"

print(text)
text = text.strip('a')
print(text)

text = "Remove set of char from end hair"
text = text.rstrip('hir')
print(text)
