def solution(a, b):
    return sum(range(min(a,b),max(a,b)+1))

'''
# 연속된 자연수들의 합 공식사용
return (abs(a-b)+1)*(a+b)/2
'''