def solution(n):
    return sum([x for x in range(1,n+1) if n % x == 0])

'''
# 자기 자신을 제외한 가장 큰 약수는 자신을 2로 나눈 수보다 작거나 같음
return num + sum([x for x in range(1,(n//2)+1) if n % x == 0])
'''