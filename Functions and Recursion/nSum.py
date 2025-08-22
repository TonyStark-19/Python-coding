# This code calculates the sum of n natural numbers using recursion

def n_Sum(n):
    # base case
    if(n == 1):
        return 1
    
    return n + n_Sum(n-1)

n = int(input("Enter the number : "))

if(n <= 0):
    print("Enter valid value only ( > 0 )")
else:
    ans = n_Sum(n)
    print("Sum is :", ans)