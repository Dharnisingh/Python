# Program to convert Json object to python object
import json
# Json data in form of string
json_obj = '{ "Name":"David", "Class":"I", "Age":6 }'
# json.loads() return python object format data
python_obj = json.loads(json_obj)
# Print the dat 
for name, val in python_obj.items():
    print(name + " : " +str(val))


