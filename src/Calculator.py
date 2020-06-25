def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

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
