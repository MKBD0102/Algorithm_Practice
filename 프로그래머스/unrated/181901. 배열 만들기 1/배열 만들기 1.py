def solution(n, k):
    return sorted([ m for m in range(1,n+1) if m % k == 0])