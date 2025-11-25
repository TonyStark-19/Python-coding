# This program implements a simple calculator using functions.

# lamda functions
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error! Division by zero."

# main calculator function
def Calculator(num1, num2, operation):
    if operation == 'add':
        return add(num1, num2)
    elif operation == 'subtract':
        return subtract(num1, num2)
    elif operation == 'multiply':
        return multiply(num1, num2)
    elif operation == 'divide':
        return divide(num1, num2)
    else:
        return "Invalid operation!"
    
# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

# Performing the calculation
result = Calculator(num1, num2, operation)

# Printing the result
print("The result is:", result)