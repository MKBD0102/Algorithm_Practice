def solution(n):
    for i in range(1,n+1):
        if n / i == i:
            return (i+1) ** 2
    return -1

'''
# 제곱근 수식 활용
def solution(n):
    x = n ** (0.5)
    if x % 1 == 0:  # 정수인지 확인
        return (x+1) ** 2
    return -1
'''