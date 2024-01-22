def solution(N, stages):
    now = [0] * (N+2)
    clear = [0] * (N+2)
    
    for s in stages:
        now[s] += 1

    for i in range(1,N+1):
        clear[i] = sum(now[i:])

    rate = [(n, now[n] / (now[n]+clear[n])) if (now[n]+clear[n]) != 0 else (n, 0) for n in range(1,N+1)]
    
    rate.sort(key=lambda x:(-x[1],x[0]))
    
    return [x[0] for x in rate]
