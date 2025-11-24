# This program Ask the user to enter two integers and one float. Convert them all to floats and print their average

int1 = int(input("Enter first integer: "))
int2 = int(input("Enter second integer: "))
flt = float(input("Enter a float: "))

average = (float(int1) + float(int2) + flt) / 3

print("The average is:", average)