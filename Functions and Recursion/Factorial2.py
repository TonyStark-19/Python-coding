# This code calculates factorial of a number using recursion

def cal_fact(n):
    # base case
    if(n == 0 or n == 1):
        return 1
    else:
        return n * cal_fact(n-1)

n = int(input("Enter the number : "))

if(n < 0):
    print("Enter valid value only ( >= 0 )")
else:
    ans = cal_fact(n)
    print("Factorial of", n , "is :", ans)