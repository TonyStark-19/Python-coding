# This code converts USD to INR using functions

def convert_to_INR(USD):
    return 87.53 * USD

USD = int(input("Enter currency value in dollar : "))

INR = convert_to_INR(USD)

print(USD, "USD =", INR , "INR")