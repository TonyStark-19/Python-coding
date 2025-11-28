# This program demonstrate the use of exception handling in Python.

try:
    x = int(input("Enter the number: "))
    ans = 10/x

except ZeroDivisionError:
    print("Dividing by zero is not possible!")

except ValueError:
    print("Enter a number only!")

else:
    print(f"Solution is {ans}")

finally:
    print("End of program!!")