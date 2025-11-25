# This program prints all numbers from starting point to ending point that are divisible by both 3 and 5.

# Taking input from the user
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))

# Printing numbers divisible by both 3 and 5
print("Numbers divisible by both 3 and 5 between", start , "and", end , "are :")

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print(num)