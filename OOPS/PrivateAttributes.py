# This program demonstrates the use of private attributes

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    # setter function
    def set_details(self, name, roll_no, marks):
        if name == "":
            print("Name cannot be empty!!")
        else:
            self.__name = name

        if roll_no < 0 or roll_no > 100:
            print("Roll number has to be between 1 and 100!!")
        else:
            self.__roll_no = roll_no

        if marks < 0:
            print("Marks cannot be negative!!")
        else:
            self.__marks = marks

    # getter function
    def get_details(self):
        print(f"Name of student is {self.__name}")
        print(f"Roll number of student is {self.__roll_no}")
        print(f"Marks of student is {self.__marks}")

s1 = Student("Aditya", 3, 95)

# print initial values
s1.get_details()

# update using setter
s1.set_details("Riya", 5, 92)

# print updated values
s1.get_details()