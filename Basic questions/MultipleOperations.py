# This program Take two numbers as input from the user and print their sum, difference, product, and quotient.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2

if num2 !=0:
    quotient = num1/num2
else:
    quotient = "undefined (cannot divide by zero)"  

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)