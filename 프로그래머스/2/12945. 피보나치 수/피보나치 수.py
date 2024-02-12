def solution(n):
    fiv = [0]*(n+1)
    i = 0
    while i < 2:
        fiv[i] = i
        i += 1
    
    for i in range(2,n+1):
        fiv[i] = fiv[i-2]+fiv[i-1]
        
    return fiv[-1] % 1234567

'''
def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1234567
'''