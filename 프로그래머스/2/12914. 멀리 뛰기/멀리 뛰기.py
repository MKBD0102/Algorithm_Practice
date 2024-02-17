def solution(n):
     
    if n == 1:
        return 1 % 1234567
    if n == 2:
        return 2 % 1234567
    
    ways = [0]*(n+1)
    
    ways[1] = 1
    ways[2] = 2
        
    for i in range(3, n+1):
        ways[i] = ways[i-1]+ways[i-2]
    
    return ways[n] % 1234567