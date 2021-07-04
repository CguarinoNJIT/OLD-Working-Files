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

def squareroot(a,round_to=8):
    result = a ** 0.5
    if not result.is_integer():
        return round(result,round_to)
    else:

        return int(result)

def square(a):
    result = a ** 2.0
    if not result.is_integer():
        return round(result,8)
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

    def square_root(self,a):
        self.result = squareroot(a)
        return self.result

    def squared(self,a):
        self.result = square(a)
        return self.result

