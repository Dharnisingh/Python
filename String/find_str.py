#The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.

text = "Find a word God from this this God string"

print(text.find("God"))

print(text.rfind("God"))

res = text.index("God")

# Find all the SubString
st = text[:]
count = 0
while "God" in st:
    count +=1
    st = st[st.find("God")+1:]
print("Count of substring God: ", count)
