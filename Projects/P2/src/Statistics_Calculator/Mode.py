

def mode(sample):

    sample.sort()
    unique_list = []
    count_list = []
    mode_list = []


    for num in sample:
        if num not in unique_list:
            unique_list.append(num)

    for unique in unique_list:
        count_list.append(sample.count(unique))

    print('Unique: ', unique_list)
    print('Count:',count_list)

    mode_index = (count_list.index(max(count_list)))
    list_mode = unique_list[mode_index]
    mode_list.append(list_mode)
    count_list.remove(max((count_list)))
    if max(count_list) in count_list:



    print(count_list)


    return mode_list


test_list = [1,2,2,2,3,4,4,4,4,4,4,5]
test_list2 = [1,1,2,3,4,5,5]
print(mode(test_list))
