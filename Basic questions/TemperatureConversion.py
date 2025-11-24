# This program Ask the user for a temperature in Celsius (string input). Convert it to , then calculate and print temperature in Fahrenheit.

celsius_input = input("Enter temperature in Celsius: ")

celcius = float(celsius_input)

fahrenheit = ((celcius * 9) /5) + 32

print("Temperature in Fahrenheit:", fahrenheit, "°F")