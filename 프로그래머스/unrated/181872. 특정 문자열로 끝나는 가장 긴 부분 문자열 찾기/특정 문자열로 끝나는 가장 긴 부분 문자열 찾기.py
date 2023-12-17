def solution(myString, pat):
    idx = myString.rfind(pat)
    return ''.join(list(myString)[:idx+len(pat)])