def solution(myString):
    return ''.join([s.lower() if s not in ["A","a"] else s.upper() for s in myString])

'''
# 모두 소문자로 바꾼 뒤 a만 A로 바꾸는 법
return myString.lower().replac('a','A')
'''