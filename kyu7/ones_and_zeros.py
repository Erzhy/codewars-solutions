def binary_array_to_number(arr):
    arr = [str(x) for x in arr]
    s = ''.join(arr)
    return int(s, 2)
