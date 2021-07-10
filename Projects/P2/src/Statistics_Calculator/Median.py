from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division

def median(sample):
    sample.sort()
    length = len(sample)
    print(f'List Length: {length}')
    centernum = int(division(2,length))
    if length % 2 == 0:
        evencenternum = int(division(2,addition(sample[centernum] , sample[subtraction(1,centernum)])))
        print(sample[centernum],sample[centernum-1])
        return evencenternum
    else:
        return sample[centernum]
