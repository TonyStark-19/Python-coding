# This code stores 9 and 9.0 in a set

# first way
# values = {9, "9.0"}

# second way is to store them in set with key
values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)