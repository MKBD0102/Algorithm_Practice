def solution(k, tangerine):
    cnt = {key:0 for key in set(tangerine)}
    
    for i in tangerine:
        cnt[i] += 1
    
    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    
    total = 0
    res = 0 
    
    for i, n in cnt:
        if total < k:
            total += n
            res += 1
        else:
            return res
    
    return res