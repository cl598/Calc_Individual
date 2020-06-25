import unittest
from CSVReader import CSVReader
from Calculator import Calculator

class CalcTest(unittest.TestCase):

    def setup(self):
        self.calc = Calculator()

    def test_calc(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_addition(self):
        files = CSVReader("/src/Addition.csv").csv_data
        for row in files:
            self.assertEqual(self.calc.add(row['Value 1'], row['Value 2']), row['Result'])
            self.assertEqual(self.calc.ans, row['Result'])

    def test_subtraction(self):
        files = CSVReader("/src/Subtraction.csv").csv_data
        for row in files:
            self.assertEqual(self.calc.subtract(row['Value 1'], row['Value 2']), row['Result'])
            self.assertEqual(self.calc.ans, row['Result'])

    def test_multiplication(self):
        files = CSVReader("/src/Multiplication.csv").csv_data
        for row in files:
            self.assertEqual(self.calc.multiple(row['Value 1'], row['Value 2']), row['Result'])
            self.assertEqual(self.calc.ans, row['Result'])

    def test_division(self):
        files = CSVReader("/src/Division.csv").csv_data
        for row in files:
            self.assertEqual(self.calc.divide(row['Value 1'], row['Value 2']), row['Result'])
            self.assertEqual(self.calc.ans, row['Result'])

    def test_results(self):
        self.assertEqual(self.calc.ans, 0)

if __name__ == '__main__':
    unittest.main()
