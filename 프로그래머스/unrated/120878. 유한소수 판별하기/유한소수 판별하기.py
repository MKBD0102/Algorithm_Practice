def solution(a, b):
    
    def gcd(a, b):
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                return i
    
    b = b // gcd(a,b)
    
    while b > 1:
        if b % 2 == 0:
            b = b // 2
        elif b % 5 == 0:
            b = b // 5
        else:
            return 2
    return 1