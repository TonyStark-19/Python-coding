# This program Take a decimal number as input and print its integer and fractional parts separately.

decimal = float(input("Enter a decimal number: "))

integer_part = int(decimal)
fractional_part = decimal - integer_part

print("Integer part:", integer_part)
print("Fractional part:", fractional_part)