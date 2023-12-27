def solution(t, p):
    n = len(p)
    m = len(t)
    cnt = 0
    for i in range(m-n+1):
        if t[i:i+n] <= p:
            cnt += 1
    return cnt