def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        char = ''
        if i % 3 == 0:
            char += 'Fizz'
        if i % 5 == 0:
            char += 'Buzz'
        result.append(char if char else i)
    return result
