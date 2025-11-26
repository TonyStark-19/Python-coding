# This program searches for an element in a list and returns its index if found.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7
is_found = False

for val in num:
    if val ==x:
        print("Element found at index:", num.index(val))
        is_found = True
        break
    else:
        continue

if not is_found:
    print("Element not found in the list.")