# This code calulate factorial of a number

n = int(input("Enter thr number : "))

prod = 1
for i in range(1, n+1):
    prod *= i

print("Factorial of" , n , "is :", prod)