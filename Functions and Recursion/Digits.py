# This program prints the digits of the number.

# function to print digits of a number
def print_digits(number):
    if number < 0:
        number = -number

    if number == 0:
        print(0)
        return
    
    digits = []

    while number > 0:
        digits.append(number % 10)
        number //= 10
    
    digits.reverse()

    for digit in digits:
        print(digit)

# Taking input from the user
num = int(input("Enter a number: "))

# Printing the digits of the number
print("The digits of the number are:")
print_digits(num)