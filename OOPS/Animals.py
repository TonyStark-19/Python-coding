# This program demonstrates Multiple Inheritance

class Herbivore:
    def eat_plants(self):
        print("Eats plants")

class Carnivore:
    def eat_meat(self):
        print("Eats meat")

class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat")

# Bear inherits from Herbivore, Carnivore, Omnivore
class Bear(Herbivore, Carnivore, Omnivore):
    def info(self):
        print("Bear is a special animal with multiple eating habits!")

# Create Bear object
b = Bear()

b.info()        # Bear's own method
b.eat_plants()  # From Herbivore
b.eat_meat()    # From Carnivore
b.eat_both()    # From Omnivore