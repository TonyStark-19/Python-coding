# This code check if number is odd or even and returns a string

def odd_or_even(n):
    if(n % 2 == 0):
        return "EVEN"
    else:
        return "ODD"
    
n = int(input("Enter your number : "))

str = odd_or_even(n)

print("The number is :", str)