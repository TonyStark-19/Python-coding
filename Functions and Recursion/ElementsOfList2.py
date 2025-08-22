# This code prints the elements of a given List using recursion

def print_elements(idx, List):
    # base case
    if(idx == len(List)):
        return
    
    print(List[idx], end=" ")
    print_elements(idx+1, List)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("List elements :")
print_elements(0, nums)