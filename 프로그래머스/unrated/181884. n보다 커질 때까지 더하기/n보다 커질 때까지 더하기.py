def solution(numbers, n):
    res = 0
    i = 0
    while res <= n:
        res += numbers[i]
        i += 1
    return res