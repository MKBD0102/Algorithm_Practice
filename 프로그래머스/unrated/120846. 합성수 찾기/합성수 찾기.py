def solution(n):
    def divnum(n):
        cnt = 0
        for i in range(1,n+1):
            if n % i == 0:
                cnt += 1
        return cnt
    cnt = 0
    for i in range(1,n+1):
        if divnum(i) >= 3:
            cnt += 1
    return cnt