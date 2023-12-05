def solution(n):
    def divnum(n):
        cnt = 0
        for i in range(1,n+1):
            if n % i == 0:
                cnt += 1
        return cnt
    cnt = 0
    for i in range(1,n+1):
        if divnum(i) >= 3:
            cnt += 1
    return cnt
'''
def solution(n):
    output = 0
# 1,2,3은 약수의 개수 2 이하 제외
    for i in range(4, n + 1): 
    
# 약수가 대칭구조이므로 제곱근까지만 확인하여 불필요한 반복 제외 
        for j in range(2, int(i ** 0.5) + 1):  

# 1과 자기 자신도 약수에 포함되므로 그 이외의 약수가 존재하면 3개 이상임 따라서 반복문을 빠져나와 불필요한 반복 제외
            if i % j == 0:
                output += 1 
                break
    return output
'''