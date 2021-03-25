def disemvowel(string):
    for i in string:
        if i in 'aeiouAEIOU':
            string = string.replace(i, '')
    return string
