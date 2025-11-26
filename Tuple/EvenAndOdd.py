# This program create tuple of even and odd numbers from a given tuple of integers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_numbers = ()
odd_numbers = ()

for num in numbers:
    if num % 2 == 0:
        even_numbers += (num,)
    else:
        odd_numbers += (num,)

print("Even numbers tuple:", even_numbers)
print("Odd numbers tuple:", odd_numbers)