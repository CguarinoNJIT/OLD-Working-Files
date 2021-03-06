import unittest
from Calculator import Calculator
from CsvReader import CsvReader
import ast
import decimal

class MyTestCase(unittest.TestCase):

# This setUp method will give scope of it's contents to the test methods that follow.
    def setUp(self) -> None:
        self.calculator = Calculator()

# This test_instantiate_calculator confirms that a Calculator Class exists.
    def test_instantiate_calculator(self) -> None:
        self.assertIsInstance(self.calculator, Calculator)

#This test_results_property_calculator confirms that the Calculator Class instantiate with default result value of 0.
    def test_results_property_calculator(self) -> None:
        self.assertEqual(self.calculator.result, 0)

# Addition Check
    def test_add_method_calculator(self) -> None:
        print("\n" , "Addition: ")
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

# Subtraction Check
    def test_subtract_method_calculator(self) -> None:
        print("\n" , "Subtraction: ")
        CsvReader.data = []
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

# Multiplication Check
    def test_multiply_method_calculator(self) -> None:
        print("\n" , "Multiplication: ")
        CsvReader.data = []
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

# Division Check
    def test_division_method_calculator(self) -> None:
        print("\n" , "Division: ")
        CsvReader.data = []
        test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(int(row['Value 1']),int(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

# Square Root Check
    def test_squareroot_method_calculator(self) -> None:
        print("\n" , "Square Root: ")
        CsvReader.data = []
        test_data = CsvReader('/src/Unit Test Square Root.csv').data
        for row in test_data:
            decimal_places = abs(decimal.Decimal((row['Result'])).as_tuple().exponent)
            self.assertEqual(self.calculator.square_root(ast.literal_eval(str(row['Value 1'])), decimal_places), ast.literal_eval(str(row['Result'])))
            self.assertEqual(self.calculator.result, float(row['Result']))

# Square Check
    def test_squared_method_calculator(self) -> None:
        print("\n" , "Squared: ")
        CsvReader.data = []
        test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squared(int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

if __name__ == '__main__':
    unittest.main()
