# This program solves whether a given string is a palindrome or not.

string = input("Enter a string: ")

string = string.lower()
reversed_string = string[::-1]

if string == reversed_string:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')