from Calculator import Division,Addition
from Support import Random_List_Generator

def median(sample):
    sample.sort()
    length = len(sample)
    print(f'List Length: {length}')
    centernum = int(Division.division(2,length))
    if length % 2 == 0:
        evencenternum = Division.division(2,Addition.addition(sample[centernum] + sample[Addition.addition(centernum,1)]))
        return sample[evencenternum]
    else:
        return sample[centernum]


testlist = Random_List_Generator.random_list_generator(10,1)
print(f'List: {testlist}')

print(median(testlist))
