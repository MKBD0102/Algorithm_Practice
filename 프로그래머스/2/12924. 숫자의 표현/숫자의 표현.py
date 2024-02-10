def solution(n):
    start = 1
    finish = 1
    total = 1
    cnt = 0
    
    while finish <= n:
        if total > n :
            total -= start
            start += 1
        elif total < n :
            finish += 1
            total += finish
        elif total == n:
            cnt += 1
            finish += 1
            total += finish
    
    return cnt