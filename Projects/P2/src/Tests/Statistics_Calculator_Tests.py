import unittest
from Calculator.Calculator import Calculator
from Statistics_Calculator.Statistics_Calculator import StatisticsCalculator
from Support.CSV_Reader import CsvReader
import ast
import decimal

class MyTestCase(unittest.TestCase):

# This setUp method will give scope of it's contents to the test methods that follow.
    def setUp(self) -> None:
        self.stats_calculator = StatisticsCalculator()

# This test_instantiate_calculator confirms that a Calculator Class exists.
    def test_instantiate_calculator(self) -> None:
        self.assertIsInstance(self.stats_calculator, StatisticsCalculator)

#This test_results_property_calculator confirms that the Calculator Class instantiate with default result value of 0.
    def test_results_property_calculator(self) -> None:
        self.assertEqual(self.stats_calculator.result, 0)

# Addition Check
    def test_add_method_calculator(self) -> None:
        print("\n" , "Addition: ")
        test_data = CsvReader('C:/Users/ChrisGuarino/Documents/IS601/Projects/P2/src/Tests/Data/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))