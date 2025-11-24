# This program Ask the user for:  Principal (P), Rate (R), Time (T). Convert all to  and compute simple interest.

principal_input = input("Enter the Principal amount (P): ")
rate_input = input("Enter the Rate amount (R) in percentage: ")
time_input = input("Enter the Time (T) in years: ")

principal = float(principal_input)
rate = float(rate_input)
time = float(time_input)

simple_interest = (principal * rate * time) / 100

print("Simple Interest is:", simple_interest)