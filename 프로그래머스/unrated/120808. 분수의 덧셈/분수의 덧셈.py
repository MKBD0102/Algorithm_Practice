def solution(numer1, denom1, numer2, denom2):
    def gcd(a,b):
        for i in range(min(a,b),0,-1):
            if a % i == 0 and b % i == 0:
                return i
    
    N = (numer1 * denom2) + (numer2 * denom1)
    D = denom1 * denom2
    
    return [ N / gcd(N,D), D / gcd(N,D) ]