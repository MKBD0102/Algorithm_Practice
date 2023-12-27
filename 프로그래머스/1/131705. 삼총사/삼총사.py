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

'''
# 리스트 컴프리헨션 사용
def solution(number):
    cnt = 0
    n = len(number)
    if n < 3:
        return cnt
    return sum(1 for i in range(n - 2) for j in range(i + 1, n - 1) for k in range(j + 1, n) if number[i]+number[j]+number[k] == 0)
'''