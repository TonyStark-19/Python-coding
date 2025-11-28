# This program demonstrates the use of method overriding (Polymorphism).

class Shape:
    def area(self):
        print("This is parent class method for area")

class Circle(Shape):
    def area(self, radius):
        area =  3.14 * radius ** 2
        print(f"Area of circle with radius {radius} is :", area)
    
class Rectangle(Shape):
    def area(self, length, breadth):
        area =  length * breadth
        print(f"Area of reactangle with length {length} and breadth {breadth} is :", area)
    
class Triangle(Shape):
    def area(self, base, height):
        area =  0.5 * base * height
        print(f"Area of triangle with base {base} and height {height} is :", area)

c = Circle()
c.area(10)

r = Rectangle()
r.area(10, 20)

t = Triangle()
t.area(10, 30)