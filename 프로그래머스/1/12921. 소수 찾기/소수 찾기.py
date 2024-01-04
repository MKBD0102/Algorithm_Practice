def solution(n):
    def is_prime(num):
        for i in range(2,int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True
    
    return sum(is_prime(x) for x in range(2,n+1))

'''
# 집합과 배수 활용
# set(range(2*i,n+1,i)): i를 제외한 i의 배수 집합
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''