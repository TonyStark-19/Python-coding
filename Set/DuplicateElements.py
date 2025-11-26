# This program from a given list, prints all elements that appear more than once in the list.

elements = [1, 2, 3, 4, 2, 5, 1, 6, 3, 7, 8, 5]
seen = set()
duplicates = set()

for element in elements:
    if element in seen:
        duplicates.add(element)
    else:
        seen.add(element)

print("Duplicate elements in the list:", duplicates)