from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Support.Random_List_Generator import random_list_generator

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


testlist = random_list_generator(10)
print(f'List: {testlist}')

print(median(testlist))
