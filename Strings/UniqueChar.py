# This program ask the user for a string and print: all unique characters and the count of unique characters.

string = input("Enter a string: ")

unique_chars = set()
for char in string:
    unique_chars.add(char)

print("Unique characters in the string:", unique_chars)
print("Count of unique characters:", len(unique_chars))