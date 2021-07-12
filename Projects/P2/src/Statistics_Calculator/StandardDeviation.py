from Statistics_Calculator.Mean import mean
from Calculator.Square import square
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.SquareRoot import squareroot
from Calculator.Division import division

def standarddeviation(sample):
    sample_mean = mean(sample)
    summation = 0
    for num in sample:
        squared_num = square(subtraction(sample_mean,num))
        summation = addition(summation,squared_num)
    mean_summation = division(len(sample),summation)
    sample_sd = squareroot(mean_summation,9)
    return sample_sd

