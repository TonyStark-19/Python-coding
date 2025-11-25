# This program takes salary as input and give the tax rates.

salary = float(input("Enter your salary: "))

tax_rate = 0

if 0 < salary < 30000:
    tax_rate = 5
elif 30000 <= salary <= 70000:
    tax_rate = 15
elif salary > 70000:
    tax_rate = 25
else:
    print("Invalid salary input")

print("Your tax rate is :", tax_rate , "%")