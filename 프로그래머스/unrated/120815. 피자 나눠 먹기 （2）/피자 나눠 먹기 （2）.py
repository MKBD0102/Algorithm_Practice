def solution(n):
    k = 1
    while 1:
        if (6 * k) % n == 0:
            return k
        else:
            k += 1