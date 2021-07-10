from Calculator import Addition,Division

def mean(sample):
    sum = 0
    for num in sample:
        sum = Addition.addition(sum,num)
    result = round(float(Division.division(len(sample),sum)),4)
    return result
