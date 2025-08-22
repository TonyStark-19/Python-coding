# This code calculates average of 3 numbers using functions

def cal_avg(a, b, c):
    sum = a + b + c
    return sum / 3

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

avg = cal_avg(a, b, c)

print("Average is :", avg)