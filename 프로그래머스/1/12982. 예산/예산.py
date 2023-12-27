def solution(d, budget):
    res = 0
    while res < len(d):
        if sum(sorted(d)[:res+1]) > budget:
            return res
        else:
            res += 1
        
    return res