def solution(number):
    n = len(number)
    comb = []
    
    if n >=  3:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    comb.append([number[i], number[j], number[k]])
    cnt = 0
    for c in comb:
        if sum(c) == 0:
            cnt += 1
    
    return cnt