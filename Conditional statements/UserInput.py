# This program continuously inputs a number from user & print if it is positive or negative until the user enters “Quit”.

while True:
    user_input = input("Enter a number (or type 'Quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Existing the program!!!")
        break

    try:
        number = float(user_input)

        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("Then number is zero.")
        
    except ValueError:
        print("Invalid input. Please enter a valid number or 'Quit' to exit.")