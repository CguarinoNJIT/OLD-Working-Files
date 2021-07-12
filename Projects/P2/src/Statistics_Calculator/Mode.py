def mode(sample):

    sample.sort()
    unique_list = []
    count_list = []
    index_list = []
    mode_list = []

    for num in sample:
        if num not in unique_list:
            unique_list.append(num)

    for unique in unique_list:
        count_list.append(sample.count(unique))

    x = max(count_list)
    for value in count_list:
        if value == x:
            index_list.append(count_list.index(value))
            count_list[count_list.index(value)] = -1

    max_index = index_list
    for index in max_index:
        mode_list.append(unique_list[index])

    return mode_list
