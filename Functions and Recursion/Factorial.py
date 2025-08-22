# This code calculates factorial of a number using functions

def cal_fact(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i

    return prod

n = int(input("Enter the number : "))

if(n < 0):
    print("Enter valid value only ( >= 0 )")
else:
    ans = cal_fact(n)
    print("Factorial of", n , "is :", ans)