import math

def solution(progresses, speeds):
    ddays = [math.ceil((100 - p)/speeds[i]) for i, p in enumerate(progresses)]
    
    res = []
    visit = []
    for i, d in enumerate(ddays):
        if i in visit:
            continue
        count = 1
        for j in range(i+1, len(ddays)):
            if ddays[j] <= d:
                count += 1
                visit.append(j)
            else:
                break
        res.append(count)
    
    return res
