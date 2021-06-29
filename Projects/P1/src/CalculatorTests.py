import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

# This setUp method will give scope of it's contents to the test methods that follow.
    def setUp(self):
        self.calculator = Calculator()
# This test_instantiate_calculator confirms that a Calculator Class exists.
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)
# Addition Check
    def test_add_method_calculator(self):
        test_data = CsvReader('Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'],row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
# Subtraction Check
    def test_subtract_method_calculator(self):
        test_data = CsvReader('Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'],row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
# Multiplication Check
    def test_multiply_method_calculator(self):
        test_data = CsvReader('Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'],row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
# Division Check
    def test_division_method_calculator(self):
        test_data = CsvReader('Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'],row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
# Square Root Check
    def test_squareroot_method_calculator(self):
        test_data = CsvReader('Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square_root(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
# Square Check
    def test_squared_method_calculator(self):
        test_data = CsvReader('Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squared(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

if __name__ == '__main__':
    unittest.main()
