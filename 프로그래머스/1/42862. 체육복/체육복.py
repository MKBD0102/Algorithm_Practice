def solution(n, lost, reserve):
    new_reserve = list(set(reserve) - set(lost))
    new_lost = list(set(lost) - set(reserve))
    
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
            continue
                
        elif i+1 in new_lost:
            new_lost.remove(i+1)
            continue
            
    return n - len(new_lost)