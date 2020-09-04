# program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sorte the list using sort methon
lst.sort(key = lambda x: x[1])
print("Sorted list = " ,lst)

# sirt the list using sorted method
new_lst = sorted(lst, key = lambda x: x[1], reverse=True)
print("Sorted New List = ", new_lst)
