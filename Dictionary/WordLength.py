# This program that create a dictionary with words as keys and their lengths as values.

words = ["apple", "banana", "kiwi", "cherry", "mango"]

word_length_dict = {}

for word in words:
    word_length_dict[word] = len(word)

print(word_length_dict)