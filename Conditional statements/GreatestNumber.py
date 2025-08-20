# This program checks which is greatest number from the numbers given by the user

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if(a > b and a > c):
    print(a, "is the greatest number")
elif(b > a and b > c):
    print(b, "is the greatest number")
elif(c > a and c > b):
    print(c, "is the greatest number")
else:
    print("All the numbers are equal")