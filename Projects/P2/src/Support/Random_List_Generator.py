import random
def random_list_generator(length=10,random_length = None,seed = None):
    random_data_list = []
    random.seed(seed)
    if random_length:
        random_sample_length = random.randrange(0,random_length)
        for num in range(0, random_sample_length):
            random_data_list.append(random.randrange(0, 101))
        return random_data_list
    else:
        for num in range(0,length):
            random_data_list.append(random.randrange(0,101))
        return random_data_list
