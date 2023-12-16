def solution(arr):
    res = []
    for n in arr:
        get = [n for i in range(n)]
        res = res+get
    return res