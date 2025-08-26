# This is a mini project : Random Password Generator

# import random for random values
import random

# import string for string constants
import string

# all values combined
charValues = string.ascii_letters + string.digits + string.punctuation

passwordLen = int(input("Enter password length (1-20): "))

if(passwordLen > 20):
    print("Enter valid length :(")
else:
    # List comprehension
    password = "".join([random.choice(charValues) for i in range(passwordLen)])
    
    print("Your random password is :", password)