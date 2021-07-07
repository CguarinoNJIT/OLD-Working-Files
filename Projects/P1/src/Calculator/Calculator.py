#Arithmatic Functions
from Addition import addition
from Subtraction import subtraction
from Multiplication import multiplication
from Division import division
from SquareRoot import squareroot
from Square import square

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self,a,b):
        self.result = addition(a,b)
        return self.result

    def subtract(self,a,b):
        self.result = subtraction(a,b)
        return self.result

    def multiply(self,a,b):
        self.result = multiplication(a,b)
        return self.result

    def divide(self,a,b):
        self.result = division(a,b)
        return self.result

    def square_root(self,a, decimal_places=8):
        self.result = squareroot(a, decimal_places)
        return self.result

    def squared(self,a):
        self.result = square(a)
        return self.result

