from Calculator import Calculator
from Statistics_Calculator.Mean import mean
from Statistics_Calculator.Median import  median
from Statistics_Calculator.Mode import mode
from Statistics_Calculator.Variance import variance
from Statistics_Calculator.StandardDeviation import standarddeviation

class StatisticsCalculator(Calculator):
    def __init__(self):
        Calculator.__init__(self)

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def median(self):
        self.result  = median(self.data)
        return self.result

    def mode(self):
        self.result = mode(self.data)
        return self.result

    def variance(self):
        self.result = variance(self.data)
        return self.result 

    def standarddeviation(self):
        self.result = standarddeviation(self.data)
        return self.result