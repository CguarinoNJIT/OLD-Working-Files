from Calculator import Calculator
from Statistics_Calculator.Mean import mean

class StatisticsCalculator(Calculator):
    def __init__(self):
        Calculator.__init__(self)

    def mean(self):
        self.result = mean(self.data)
        return self.result
