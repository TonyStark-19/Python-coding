# This code adds and subtracts complex numbers using Dunder functions ( __ ) : operator overloading

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(self.real, "i +", self.imag, "j")
    
    # Dunder function for adding
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)
    
    # Dunder function for subtracting
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal, newImag)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()