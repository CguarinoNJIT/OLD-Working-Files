from Calculator import Calculator
from Statistics_Calculator.Mean import mean
from Statistics_Calculator.Median import  median
from Statistics_Calculator.Mode import mode
from Statistics_Calculator.Variance import variance
from Statistics_Calculator.StandardDeviation import standarddeviation

__all__ = ['StatisticsCalculator']

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

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        if isinstance(new_data, list) and new_data == []:
            raise Exception(f'ERROR: {new_data} cannot be empty list')
        self._data = new_data

