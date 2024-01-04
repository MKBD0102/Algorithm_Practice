def solution(n):
    def is_prime(num):
        for i in range(2,int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True
    
    return sum(is_prime(x) for x in range(2,n+1))