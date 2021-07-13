#Arithmatic Functions

class Add:
    @staticmethod
    def addition(a,b):
        return a + b

class Subtract:
    @staticmethod
    def subtraction(a,b):
        return b - a

class Multiplication:
    @staticmethod
    def multiplication(a,b):
        return a * b

class Division:
    @staticmethod
    def division(a,b):
        result = b / a
        if not result.is_integer():
            return round(result,9)
        else:
            return int(result)

class SquareRoot:
    @staticmethod
    def squareroot(a, decimal_places=8):
        result = a ** 0.5
        if not result.is_integer():
            result = round(result, decimal_places)
        else:
            result = int(result)
        return result

class Square:
    @staticmethod
    def square(a):
        result = a ** 2.0
        if not result.is_integer():
            return round(result,9)
        else:
            return int(result)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self,a,b):
        self.result = Add.addition(a,b)
        return self.result

    def subtract(self,a,b):
        self.result = Subtract.subtraction(a,b)
        return self.result

    def multiply(self,a,b):
        self.result = Multiplication.multiplication(a,b)
        return self.result

    def divide(self,a,b):
        self.result = Division.division(a,b)
        return self.result

    def square_root(self,a, decimal_places=8):
        self.result = SquareRoot.squareroot(a, decimal_places)
        return self.result

    def squared(self,a):
        self.result = Square.square(a)
        return self.result

