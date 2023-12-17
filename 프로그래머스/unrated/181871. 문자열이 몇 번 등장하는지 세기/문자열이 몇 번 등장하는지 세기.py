def solution(myString, pat):
    cnt = 0
    for i in range(myString.find(pat),len(myString)):
        if myString[i:].find(pat) == 0:
            cnt += 1
    return cnt


'''
# startswith 함수 사용
def solution(myString, pat):
    cnt = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :  # startswith() return True/False
            cnt += 1
    return cnt

'''