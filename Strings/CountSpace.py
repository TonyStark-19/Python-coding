# This program takes a string from the user and prints the number of spaces in the string

string = input("Enter a string: ")

space_count = 0
for char in string:
    if char == ' ':
        space_count += 1

print("Number of spaces in the string:", space_count)