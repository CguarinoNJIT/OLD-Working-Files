import unittest
import numpy
import statistics
from Support.Random_List_Generator import random_list_generator
from Support.ListToString import list2string
from Statistics_Calculator.Statistics_Calculator import StatisticsCalculator

class MyTestCase(unittest.TestCase):

# This setUp method will give scope of it's contents to the test methods that follow.
    def setUp(self) -> None:
        self.stats_calculator = StatisticsCalculator()
        test_data = random_list_generator(10)
        self.stats_calculator.data = test_data

    # This test_instantiate_calculator confirms that a Calculator Class exists.
    def test_instantiate_calculator(self) -> None:
        self.assertIsInstance(self.stats_calculator, StatisticsCalculator)

#This test_results_property_calculator confirms that the Calculator Class instantiate with default result value of 0.
    def test_results_property_calculator(self) -> None:
        self.assertEqual(self.stats_calculator.result, 0)

#Check for an Empty List
    def test_empty_test_data(self) -> None:
        self.assertNotEqual(len(self.stats_calculator.data),0)

#Check for valid numbers.
    def test_valid_number(self) -> None:
        self.assertTrue(list2string(self.stats_calculator.data).isdigit())

#Check for a list length > 1- Zero Divide Check.
    def test_valid_list_length(self) ->None:
        self.assertGreater(len(self.stats_calculator.data),1)

# Mean Check
    def test_mean_method_statistics_calculator(self) -> None:
        print("\n" , "Mean: ")
        check_num = round(numpy.mean(self.stats_calculator.data),4)
        test_num = self.stats_calculator.mean()
        self.assertEqual(test_num, check_num)
        print(self.stats_calculator.data)
        print(f"Pass: {check_num} = {test_num}")

#Median Check
    def test_median_method_statistics_calculator(self) ->None:
        print("\n","Median:")
        check_num = numpy.median(self.stats_calculator.data)
        test_num = self.stats_calculator.median()
        self.assertEqual(test_num, check_num)
        print(self.stats_calculator.data)
        print(f"Pass: {check_num} = {test_num}")

#Mode
    def test_mode_method_statistics_calculator(self) ->None:
        print("\n","Mode:")
        check_num = statistics.multimode(self.stats_calculator.data)
        test_num = self.stats_calculator.mode()
        check_num.sort()
        self.assertEqual(test_num,check_num)
        print(self.stats_calculator.data)
        print(f'Pass: {check_num} = {test_num}')

#Variance
    def test_variance_method_statistics_calculator(self) ->None:
        print("\n","Variance:")
        check_num = round(statistics.variance(self.stats_calculator.data),9)
        test_num = self.stats_calculator.variance()
        self.assertEqual(test_num,check_num)
        print(self.stats_calculator.data)
        print(f"Pass: {check_num} = {test_num}")

#Standard Deviation
    def test_standarddeviation_method_statistics_calculator(self) ->None:
        print("\n","Standard Deviation:")
        check_num = round(numpy.std(self.stats_calculator.data),9)
        test_num = self.stats_calculator.standarddeviation()
        self.assertEqual(test_num, check_num)
        print(self.stats_calculator.data)
        print(f"Pass: {check_num} = {test_num}")

