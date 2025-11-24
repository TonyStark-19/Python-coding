# This program swap values of two numbers entered by the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Swapping the values

temp = num1
num1 = num2
num2 = temp

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)