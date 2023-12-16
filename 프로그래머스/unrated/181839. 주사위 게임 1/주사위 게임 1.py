def solution(a, b):
    if (a + b) % 2 == 0:
        if a % 2 == 0:
            return abs(a - b)
        else:
            return a ** 2 + b ** 2
    else:
        return 2 * (a+b)