def solution(balls, share):
    num = 1
    den1 = 1
    den2 = 1
    for i in range(1,balls+1):
        num *= i
    for i in range(1,(balls - share)+1):
        den1 *= i
    for i in range(1,share+1):
        den2 *= i
    return num/(den1*den2)