# 1: using in or not in keyword
# 2: using find() method
# 3: using index() method

text = "I am soure string holding some text so that one can be found using some string methods"

trg = "holding"

if trg in text:
    print("String :{} found".format(trg))
else:
    print("String :{} not found".format(trg))

index = text.find(trg)
if index != -1:
    print("String : {} found at index {}".format(trg,index))
else:
    print("String : {} not found index {}".format(trg,index))

result = text.index(trg, 0, len(text))
print("String : {} found at {}".format(trg,result))

result = text.index(trg);
print("String : {} found at {}".format(trg,result))
