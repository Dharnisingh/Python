# Python program to convert Python object to JSON data
import json

python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}

# json.dumps() methd convert python_obj to json fromat and return the same
json_data = json.dumps(python_obj)
# Print json_data
print("Json Data:\n", json_data)

