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

    def test_results(self):
        self.assertEqual(self.calc.ans, 0)

if __name__ == '__main__':
    unittest.main()
