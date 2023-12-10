def solution(number):
    return int(number) % 9

'''
# 문제 의도 활용(각 자리 숫자 합을 9로 나눈 나머지)
return sum([int(n) for n in number]) % 9
'''