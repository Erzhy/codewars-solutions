def even_numbers_before_fixed(sequence, fixed_element):
    count = 0
    for i in sequence:
        if i == fixed_element:
            break
        elif i % 2 == 0:
            count += 1
    else:
        return -1
    return count
