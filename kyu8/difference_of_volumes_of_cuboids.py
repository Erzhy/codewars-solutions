def find_difference(a, b):
    vol_1, vol_2 = 1, 1
    for i in a:
        vol_1 *= i
    for i in b:
        vol_2 *= i
    return abs(vol_1 - vol_2)
