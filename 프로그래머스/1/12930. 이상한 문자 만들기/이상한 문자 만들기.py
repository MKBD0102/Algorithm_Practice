def solution(s):
    j = 0
    res = ''
    for i in range(len(s)):
        if s[i] == ' ':
            res += s[i]
            j = 0            
        elif j % 2 == 0:
            res += s[i].upper()
            j += 1
        elif j % 2 != 0:
            res += s[i].lower()
            j += 1
    return res

'''
# split(): 모든 공백 제거 분리, split(' '): 공백 하나만 제거 분리
# 리스트 컴프리헨션 사용
return ' '.join([[c.upper() if i % 2 == 0 else c.lower() for i,c in enumerate(word)] for word in s.split(' ')])

'''

