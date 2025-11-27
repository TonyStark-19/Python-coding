# This program demonstrates differnt types of methods in Python OOP

class Laptop:
    # class variable
    storage_type = "SSD"

    # contstructor
    def __init__(self, RAM, storage):
        # instance variables
        self.RAM = RAM
        self.storage = storage

    # class method
    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")

    # instance method
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage} {self.storage_type}")

    # static method
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"Final price after {discount}% discount is: {final_price}")

# creating object of Laptop class
l1 = Laptop("16GB", "1TB")
l2 = Laptop("8GB", "512GB")

# calling instance method
l1.get_info()
l2.get_info()

# calling class method
Laptop.get_storage_type()

# calling static method
Laptop.calc_discount(40_000, 10)