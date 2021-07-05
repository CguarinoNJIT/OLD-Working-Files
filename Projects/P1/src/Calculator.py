import decimal

def addition(a,b):
    return a + b

def subtraction(a,b):
    return b - a

def multiplication(a,b):
    return a * b

def division(a,b):
    result = b / a
    if not result.is_integer():
        return round(result,9)
    else:
        return int(result)

def squareroot(a, decimal_places=8):
    result = a ** 0.5
    if not result.is_integer():
        result = round(result, decimal_places)
    else:
        result = int(result)
    return result

def square(a, decimal_places=8):
    result = a ** 2.0
    if not result.is_integer():
        return round(result, decimal_places)
    else:
        return int(result)

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

    def squared(self,a, decimal_places=8):
        self.result = square(a, decimal_places)
        return self.result

