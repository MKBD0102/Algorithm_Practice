def solution(n):
    def fact(n):
        mul = 1
        for i in range(1,n+1):
            mul *= i
        return mul
    maxi = 0
    for i in range(1,n+1):
        if fact(i) > n:
            return maxi
        elif fact(i) <= n and fact(i) > maxi:
            maxi = i
    return maxi

'''
# 팩토리얼 함수 정의로 생긴 불필요한 반복문 제거
def solution(n):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial = factorial * answer
    answer -= 1
    return answer
'''