# This program takes a string input from the user and converts it into an integer and a float, then prints them.

user_input = input("Enter a number: ")

int_value = int(user_input)
float_value = float(user_input)
string_value = str(user_input)

print("Integer value:" , int_value, "| type: ", type(int_value))
print("Float value:" , float_value, "| type: ", type(float_value))
print("String value:" , string_value, "| type: ", type(string_value))