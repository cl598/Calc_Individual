def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def square(a):
    return a * a

def squareroot(a):
    return a**(1/2)

class Calculator:

    ans = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.ans = addition(a, b)
        return self.ans

    def subtract(self, a, b):
        self.ans = subtraction(a, b)
        return self.ans

    def multiple(self, a, b):
        self.ans = multiplication(a, b)
        return self.ans

    def divide(self, a, b):
        self.ans = division(a, b)
        return self.ans

    def squaring(self, a):
        self.ans = square(a)
        return self.ans

    def squarerooting(self, a):
        self.ans = squareroot(a)
        return self.ans