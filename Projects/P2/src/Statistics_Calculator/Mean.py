def mean(sample):
    sum = 0
    for num in sample:
        sum += num
    result = sum/len(sample)
    return result