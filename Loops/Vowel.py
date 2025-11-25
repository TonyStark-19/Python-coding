# This program counts the number of vowels in a given string.

string = input("Enter a string: ")

vowel_count = 0

for ch in string.lower():
    if ch in 'aeiou':
        vowel_count += 1

print("Number of vowels in the given string is:", vowel_count)