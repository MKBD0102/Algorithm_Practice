def solution(left, right):
    def divisor_num(n):
        cnt = 1
        for i in range(1,n//2+1):
            if n % i == 0:
                cnt += 1
        return cnt
    ans = 0
    for n in range(left,right+1):
        if divisor_num(n) % 2 == 0:
            ans += n
        else:
            ans -= n
    return ans
    
    