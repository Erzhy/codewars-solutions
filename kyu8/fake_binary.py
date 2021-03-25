def fake_bin(x):
    result = ''
    for i in x:
        if i < '5':
            result += '0'
        else:
            result += '1'
    return result
