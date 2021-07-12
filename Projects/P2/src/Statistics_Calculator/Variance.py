from Statistics_Calculator.Mean import mean
from Calculator.Square import square
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division

def variance(sample):
    sample_mean = mean(sample)
    summation = 0
    for num in sample:
        squared_num = square(subtraction(sample_mean,num))
        summation = addition(summation,squared_num)
    sample_variance = division(subtraction(1,len(sample)),summation)
    return sample_variance


