# This program Inputs two lists of integers from the user. Merge them into one list and sort the result.

# Input first list
list1 = []
n1 = int(input("Enter number of elements in first list: "))

for i in range(n1):
    element = int(input(f"Enter element {i+1} of first list: "))
    list1.append(element)

# Input second list
list2 = []
n2 = int(input("Enter number of elements in second list: "))

for i in range(n2):
    element = int(input(f"Enter element {i+1} of second list: "))
    list2.append(element)

# Merge the two lists
merged_list = list1 + list2

# sort the merged list
merged_list.sort()

print("Merged and sorted list:" , merged_list)