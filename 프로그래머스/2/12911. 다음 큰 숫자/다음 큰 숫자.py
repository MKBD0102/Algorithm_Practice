def solution(n):
    def get_ones(num):
        s = ''
        cnt = 0
        while num > 0:
            r = num % 2
            num = num // 2
            if r == 1:
                cnt += 1

        return cnt
    
    for i in range(n+1, 1000001):
        if get_ones(n) == get_ones(i):
            return i
'''
# 이진수 구하는 함수 bin
def solution(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n
'''