# find max in a list

def max_elem(l):
    max = 0
    for i in l:
        if i > max:
            max = i
    return max

l = [ x for x in range(20) if x%2 != 0]

res = max_elem(l)
print("List :", l)
print("Max eleme: ", res)
