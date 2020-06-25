from CSVReader import CSVReader

def addition(a, b):
    return a + b

class Calculator:

    ans = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.ans = addition(a, b)
        return self.ans

