# This program checks whether two lists share no common elements.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 8, 9, 10]

common_elements = set(list1) & set(list2)

if not common_elements:
    print("The two lists have no common elements.")
else:
    print("The two lists have common elements:", common_elements)