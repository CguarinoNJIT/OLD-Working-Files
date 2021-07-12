from Calculator import Calculator
from Statistics_Calculator.Mean import mean
from Statistics_Calculator.Median import  median

class StatisticsCalculator(Calculator):
    def __init__(self):
        Calculator.__init__(self)

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def median(self):
        self.result  = median((self.data))
        return self.result