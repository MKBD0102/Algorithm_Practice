def solution(order):
    return len([n for n in list(map(int,str(order))) if n in [3,6,9]])