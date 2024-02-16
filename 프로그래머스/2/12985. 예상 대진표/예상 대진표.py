def solution(n,a,b):
    num_round = 1
    
    while abs(a-b) > 1 or (a-1)//2 != (b-1)//2:
        a = (a-1)//2 + 1
        b = (b-1)//2 + 1
        num_round += 1
    return num_round