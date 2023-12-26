'''
def solution(n, m):
    def gcd(a,b):
        for i in range(min(a,b),0,-1):
            if a % i == 0 and b % i == 0:
                return i
    def lcm(a,b):
        for i in range(max(a,b),a*b+1):
            if i % a == 0 and i % b == 0:
                return i
    return [gcd(n,m),lcm(n,m)]

'''
# 최소공배수 = 두 수 곱 * 최대공약수
def solution(n, m):
    a,b = max(n, m), min(n, m)
    while b:
        a,b = b,a%b
    return [a,n*m//a]
