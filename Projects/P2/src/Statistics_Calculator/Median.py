from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division

def median(sample):
    sample.sort()
    length = len(sample)
    print(f'List Length: {length}')
    centernum = int(division(2,length))
    if length % 2 == 0:
        evencenternum = (division(2,addition(sample[centernum] , sample[subtraction(1,centernum)])))
        return evencenternum
    else:
        return sample[centernum]
