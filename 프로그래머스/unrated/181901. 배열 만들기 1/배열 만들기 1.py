def solution(n, k):
    return sorted([ m for m in range(1,n+1) if m % k == 0])

'''
# for문 안쓰고
return list(range(k,n+1,k))
'''