# This program check if the given number is a multiple of 7 or not

number = int(input("Enter number : "))

if(number % 7 == 0):
    print("The number", number , "is a multiple of 7")
else:
    print("The number", number , "is not a multiple of 7")