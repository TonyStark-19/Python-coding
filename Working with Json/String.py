# This program demonstrates the working of json with python when working with string.

# import json module
import json

# python object (dictionary)
pyt_obj1 = {
    "name": "Aditya",
    "isStudent": True
}
print(type(pyt_obj1), pyt_obj1)

# coverting to json
json_str1 = json.dumps(pyt_obj1)
print(type(json_str1), json_str1)
print()

# json string
json_str2 = '{"name": "Aditya", "isStudent": true}'
print(type(json_str2), json_str2)

# coverting to python object
pyt_obj2 = json.loads(json_str2)
print(type(pyt_obj2), pyt_obj2)