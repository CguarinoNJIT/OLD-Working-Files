def squareroot(a, decimal_places=8):
    result = a ** 0.5
    if not result.is_integer():
        result = round(result, decimal_places)
    else:
        result = int(result)
    return result