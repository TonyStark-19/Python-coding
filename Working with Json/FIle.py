# This program demonstrates the working of json with python when working with files.

# import json module
import json

# load the file
with open("Working with Json/data.json") as f:
    # json to python object
    pyt_obj = json.load(f)
    print(pyt_obj)

# dictionary (python object)
data = {
    "name": "Aditya",
    "age": 20,
    "isStudent": True
}

# new file
with open("Working with Json/data2.json", "w") as f:
    # python object to json
    json.dump(data, f, indent=4, sort_keys=True)