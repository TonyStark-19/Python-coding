# This program demonstrates Constructor Overloading Using Default Parameters

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def show_details(self):
        print("Person Details:")
        print(f"Name: {self.name}")
        
        if self.age is not None:
            print(f"Age: {self.age}")
        else:
            print("Age: Not provided")

        if self.address is not None:
            print(f"Address: {self.address}")
        else:
            print("Address: Not provided")

# Only name
p1 = Person("Aditya")
p1.show_details()
print()

# Name + age
p2 = Person("Aditya", 20)
p2.show_details()
print()

# Name + age + address
p3 = Person("Aditya", 20, "Delhi, India")
p3.show_details()