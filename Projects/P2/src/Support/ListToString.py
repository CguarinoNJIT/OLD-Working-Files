def list2string(given_list):
    new_string = ''
    convert = [str(element) for element in given_list]
    for element in convert:
        new_string += element
    return new_string
