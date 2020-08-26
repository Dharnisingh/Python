# Remove duplicate from list

l1 = [x for x in range(10)]
l2 = [x for x in range(15) if x%2 !=0]

l3 = l1+l2
print("List :", l3)

def rmv_dup(l):
    for i in l:
        if l.count(i)>1:
            del l[i]
    return l

res = rmv_dup(l3)
print("Result: ", res)

# Secomd approach
res = set(l3) 
print("Using set method: ", res)
