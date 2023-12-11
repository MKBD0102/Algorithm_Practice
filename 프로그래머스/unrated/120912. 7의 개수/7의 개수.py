def solution(array):
    cnt = 0
    for n in array:
        cnt += str(n).count('7')
    return cnt

'''
# list에 str() 씌우면 문자열 됨
return str(array).count('7')
'''