def random_list_generator():
    import random
    random_data_list = []
    random_sample_length = random.randrange(0,101)
    for num in range(0,random_sample_length):
        random_data_list.append(random.randrange(0,101))
    return random_data_list

def mean(sample):
    sum = 0
    for num in sample:
        sum += num
    result = sum/len(sample)
    return result

testlist = random_list_generator()
testmean = mean(testlist)
print(testmean)