# This program takes two integers and prints all even numbers between them (inclusive) using a function.

# function to get even numbers in the inclusive range
def inclusive_range(start, end):
    even_numbers = []

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

# Taking input from the user
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))

# Getting the even numbers in the inclusive range
even_numbers = inclusive_range(start, end)

# Printing the even numbers
print("Even numbers between", start , "and", end , "are : " , even_numbers)