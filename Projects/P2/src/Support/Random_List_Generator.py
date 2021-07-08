def random_list_generator():
    import random
    random_data_list = []
    random_sample_length = random.randrange(0,101)
    for num in range(0,random_sample_length):
        random_data_list.append(random.randrange(0,101))
    return random_data_list