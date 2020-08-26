# Sort list of tuple using lambda

list_tup = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sdata = sorted(list_tup, key=lambda x: x[1])
print(sdata)

# sort a list of dictionaries using Lambda
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)
