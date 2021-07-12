import unittest
import numpy
import statistics
from Calculator.Calculator import Calculator
from Statistics_Calculator.Statistics_Calculator import StatisticsCalculator
from Support.CSV_Reader import CsvReader
from Support.Random_List_Generator import random_list_generator
from Statistics_Calculator.Mean import mean
from Statistics_Calculator.Median import median
from Statistics_Calculator.Mode import mode
from Statistics_Calculator.Variance import variance
import ast
import decimal

test_list = [1,2,2,3,4,4,5]

class MyTestCase(unittest.TestCase):

# This setUp method will give scope of it's contents to the test methods that follow.
    def setUp(self) -> None:
        self.stats_calculator = StatisticsCalculator()
        self.test_data = random_list_generator(10,0,1)

# This test_instantiate_calculator confirms that a Calculator Class exists.
    def test_instantiate_calculator(self) -> None:
        self.assertIsInstance(self.stats_calculator, StatisticsCalculator)

#This test_results_property_calculator confirms that the Calculator Class instantiate with default result value of 0.
    def test_results_property_calculator(self) -> None:
        self.assertEqual(self.stats_calculator.result, 0)

#Check for valid numbers.
# - Error handling and throw a TypeError if wrong result type is being tried to process.
# isdigit or isnum - String methods may not work.
#use a while loop and break if it is false?

#Check for empty list.

#Check for Zero Divide

#Error Handling

# try:
#     pass
# except:
#     pass
# else:
#     pass

# Mean Check
    def test_mean_method_statistics_calculator(self) -> None:
        print("\n" , "Mean: ")
        print(self.test_data)
        check_num = numpy.mean(self.test_data)
        test_num = mean(self.test_data)
        if test_num == check_num:
            print(f"Pass: {check_num} = {test_num}")
        else:
            print(f"Hey the expected median of this list is {check_num} not {test_num} stupid...Fix it!")

#Median Check
    def test_median_method_statistics_calculator(self) ->None:
        print("\n","Median:")
        print(self.test_data)
        check_num = numpy.median(self.test_data)
        test_num = median(self.test_data)
        if test_num == check_num:
            print(f"Pass: {check_num} = {test_num}")
        else:
            print(f"Hey the expected median of this list is {check_num} not {test_num} stupid...Fix it!")

#Mode
    def test_mode_method_statistics_calculator(self) ->None:
        print("\n","Mode:")
        print(self.test_data)
        check_num = statistics.multimode(self.test_data)
        test_num = mode(self.test_data)
        if test_num == check_num:
            print(f"Pass: {check_num} = {test_num}")
        else:
            print(f"Hey the expected mode of this list is {check_num} not {test_num} stupid...Fix it!")

#Variance
    def test_variance_method_statistics_calculator(self) ->None:
        print("\n","Variance:")
        print(self.test_data)
        check_num = round(statistics.variance(self.test_data),9)
        test_num = variance(self.test_data)
        if test_num == check_num:
            print(f"Pass: {check_num} = {test_num}")
        else:
            print(f"Hey the expected variance of this list is {check_num} not {test_num} stupid...Fix it!")

# Work on randomly generating datasets so that you can test the stats calc... 