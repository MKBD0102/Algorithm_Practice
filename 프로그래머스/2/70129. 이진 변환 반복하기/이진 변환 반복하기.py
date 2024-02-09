def solution(s):
    zero = 0
    cnt = 0
    while s != '1':
        zero += s.count('0')
        trans = s.maketrans({'0':''})
        s = s.translate(trans)
        c = len(s)
        res = ''
        while c > 0:
            d = c % 2
            c = c // 2
            res = str(d) + res
        s = res
        cnt += 1
    return [cnt, zero]

'''
# 0을 제거한 문자열의 길이 = 1의 개수
def solution(s):
    zero = 0
    cnt = 0
    while s != '1':
    
        zero += s.count('0')
        c = s.count('1')
        
        res = ''
        while c > 0:
            d = c % 2
            c = c // 2
            res = str(d) + res
        
        s = res
        cnt += 1
    return [cnt, zero]
'''