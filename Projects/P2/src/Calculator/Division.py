def division(a, b):
    result = b / a
    if not result.is_integer():
        return round(result, 9)
    else:
        return int(result)