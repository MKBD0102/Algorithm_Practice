def solution(myString):
    return sorted((' '.join(myString.split('x'))).split())

'''
# 조건문 활용
def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch)
'''