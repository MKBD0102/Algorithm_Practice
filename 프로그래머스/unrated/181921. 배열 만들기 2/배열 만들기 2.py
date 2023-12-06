def solution(l, r):
    answer = []
    for n in range(l,r+1):
        if n % 5 == 0:
            if len(set([int(s) for s in str(n)]) - set([0,5])) == 0:
                answer.append(n)
        
    return [-1] if answer == [] else answer

'''
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
# 문자열을 set()에 넣으면 각 문자가 set의 원소가 됨 ex) set('hello') -> {'h','e','l','o'}
# (not 차집합)이 공집합이면 True, 공집합이 아니면 False 반환됨    
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]

'''