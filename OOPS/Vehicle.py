# This program demonstrates use of inheritance

class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")

class Car(Vehicle):
    def __init__(self, brand, model, price, seats):
        super().__init__(brand, model, price)
        self.seats = seats

    def show_car_info(self):
        self.show_info()
        print(f"Seats: {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, model, price, engine_cc):
        super().__init__(brand, model, price)
        self.engine_cc = engine_cc

    def show_bike_info(self):
        self.show_info()
        print(f"Engine CC: {self.engine_cc}")

# Creating objects
car1 = Car("Toyota", "Innova", 2500000, 7)
bike1 = Bike("Royal Enfield", "Classic 350", 180000, 350)

# Displaying details
print("Car Details:")
car1.show_car_info()

print("\nBike Details:")
bike1.show_bike_info()