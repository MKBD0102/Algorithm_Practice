def solution(a, b, n):
    total = n
    res = 0
    while total >= a:
        get = (total // a) * b
        total = get + (total % a)
        res += get
    return res