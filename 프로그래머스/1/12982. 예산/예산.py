''''
def solution(d, budget):
    res = 0
    d = sorted(d)
    while res < len(d):
        if sum(d[:res+1]) > budget:
            return res
        else:
            res += 1        
    return res

'''
# 리스트 슬라이싱 -> 오버헤드 위험
def solution(d, budget):
    hap = 0
    res = 0
    d.sort()

    for i in range(len(d)):
        hap += d[i]
        if hap > budget:
            break
        else:
            res += 1
    return res
