def solution(myString):
    return ''.join([s.lower() if s not in ["A","a"] else s.upper() for s in myString])