# This code calulate sum of n numbers

n = int(input("Enter range of sum : "))

sum = 0
for i in range(1, n+1):
    sum += i

print("Sum is :", sum)