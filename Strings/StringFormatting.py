# This program demonstrates various string formatting techniques in Python.

a = 5
b = 10
sum = a + b

# normal formatting
print("Language is {}".format("Python"))
print("Sum of {} and {} is {}".format(a, b, sum))

# index-based formatting
print("Sum of {1} and {0} is {2}".format(a, b, sum))

# value based formatting
print("Values of vars {a} and {b}".format(a=7, b=8))

# f-string formatting
print(f"Sum of {a} and {b} is {sum}")