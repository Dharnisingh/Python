# Reading json file
import json

#open and read from json file
with open('json_file.json','r') as f:
    # Returns data in form of dictionary
    data = json.load(f)
    print("Print json records: ")
    for k,val in data.items():
        print("key: ", k)
        # Print values
        for v in val:
            print(v)
        
