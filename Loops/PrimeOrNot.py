# This program if a number is prime or not using function or loops.

def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False
    
# Taking input from the user
num = int(input("Enter the number: "))

# checking if number is prime or not
is_prime = is_prime(num)

if is_prime:
    print("The number", num , "is a prime number!")
else:
    print("The number", num , "is not a prime number!!")