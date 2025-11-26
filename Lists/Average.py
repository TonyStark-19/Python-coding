# This program calculates the average of a list of numbers.

number = [10, 20, 30, 40, 50]

total = 0
for val in number:
    total += val

average = total / len(number)

print("Average of the list is:", average)