# This program counts the number of digits of a number and also returns the sum of the digits.

# function to count digits and sum of digits
def count_and_sum_digits(number):
    if number < 0:
        number = -number

    if number == 0:
        print(0)
        return
    
    digits_sum = 0
    digits_count = 0

    while number > 0:
        digits_sum += number % 10
        number //= 10
        digits_count += 1
    
    return digits_count, digits_sum

# Taking input from the user
num = int(input("Enter a number: "))

# Getting the count and sum of digits
count, total_sum = count_and_sum_digits(num)

# Printing the count and sum of digits
print("The number of digits is:", count)
print("The sum of the digits is:", total_sum)