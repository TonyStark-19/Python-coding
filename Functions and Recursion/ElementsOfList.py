# This code prints the elements of a given List using functions

def print_elements(List):
    for el in List:
        print(el, end=" ")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("List elements :")
print_elements(nums)