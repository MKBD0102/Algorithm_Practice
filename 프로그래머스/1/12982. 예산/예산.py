def solution(d, budget):
    res = 0
    d = sorted(d)
    while res < len(d):
        if sum(d[:res+1]) > budget:
            return res
        else:
            res += 1
        
    return res