import unittest
from Calculator.Calculator import Calculator
from Statistics_Calculator.Statistics_Calculator import StatisticsCalculator
from Support.CSV_Reader import CsvReader
from Support.Random_List_Generator import random_list_generator
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
        test_data = CsvReader('Data/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.stats_calculator.add(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.stats_calculator.result, int(row['Result']))

# Mean Check
    def test_mean_method_statistics_calculator(self) -> None:
        print("\n" , "Mean: ")
        test_data = random_list_generator()
        for num in test_data:


# Work on randomly generating datasets so that you can test the stats calc... 