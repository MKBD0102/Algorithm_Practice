def solution(x):
    sum_x = sum(map(int,str(x)))
    return x % sum_x == 0