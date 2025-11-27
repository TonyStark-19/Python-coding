# This program creates a product store using OOP concepts in Python

class Product:
    # track total products
    count = 0

    # constructor
    def __init__(self, name, price):
        # instance variables
        self.name = name
        self.price = price
        # increment product count
        Product.count += 1

    # instance method
    def get_info(self):
        print(f"Product Name: {self.name}, Price: Rs.{self.price}")

    # class method
    @classmethod
    def get_total_products(cls):
        print(f"Total products in store = {cls.count}")

    # static method
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"Final price after {discount}% discount is: {final_price}")

p1 = Product("Smartphone", 10_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Pen", 10)

p2.get_info()

Product.get_total_products()

p3.calc_discount(p1.price, 15)