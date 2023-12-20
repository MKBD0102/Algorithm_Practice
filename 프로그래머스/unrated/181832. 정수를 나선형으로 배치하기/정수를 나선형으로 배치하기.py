def solution(n):
    arr = [[0]*n for _ in range(n)]
    
    u, d, l, r = 0, n-1, 0, n-1
    num = 1
    
    while u <= d and l <= r:
        for i in range(l, r+1):
            arr[u][i] = num
            num += 1
        u += 1
        
        for i in range(u, d+1):
            arr[i][r] = num
            num += 1
        r -= 1
        
        if u <= d:
            for i in range(r,l-1,-1):
                arr[d][i] = num
                num += 1
            d -= 1
        
        if l <= r:
            for i in range(d, u-1,-1):
                arr[i][l] = num
                num += 1
            l += 1

    return arr 
                
            
    