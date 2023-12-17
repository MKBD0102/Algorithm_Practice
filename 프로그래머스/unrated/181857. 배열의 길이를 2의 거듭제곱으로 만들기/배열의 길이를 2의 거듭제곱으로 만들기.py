def solution(arr):
    n = len(arr)
    if n&(n-1) == 0:
        return arr
    else:
        r = 2**len(bin(n)[2:]) - n
        arr += [0 for i in range(r)]
        return arr