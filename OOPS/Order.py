# This code creates class Order and use a Dunder function to compare price

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # Dunder function
    def __gt__(self, ordr2):
        return self.price > ordr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)