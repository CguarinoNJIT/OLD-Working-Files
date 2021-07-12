def square(a):
    result = a ** 2.0
    if not result.is_integer():
        return round(result, 9)
    else:
        return int(result)
