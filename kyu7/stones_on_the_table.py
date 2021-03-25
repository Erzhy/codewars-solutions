def solution(stones):
    count = 0
    prev_stone = ''
    for i in stones:
        if i == prev_stone:
            count += 1
        prev_stone = i
    return count
