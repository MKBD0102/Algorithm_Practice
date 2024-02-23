def solution(citations):
    max_h = 0
    
    for i in range(10000):
        if i > max(citations):
            return max_h
        
        cnt = sum([1 if c >= i else 0 for c in citations])
        
        if cnt >= i:
            max_h = i
    
    return max_h