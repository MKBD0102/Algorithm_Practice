def solution(n):
    return sum(list(map(int, str(n))))

'''
# 재귀 함수 사용
def solution(n):
    if n < 10:
        return n
    return n % 10 + solution(n // 10)
'''