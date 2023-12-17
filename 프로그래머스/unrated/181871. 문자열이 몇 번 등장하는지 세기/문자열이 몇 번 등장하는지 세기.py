def solution(myString, pat):
    cnt = 0
    for i in range(myString.find(pat),len(myString)):
        if myString[i:].find(pat) == 0:
            cnt += 1
    return cnt