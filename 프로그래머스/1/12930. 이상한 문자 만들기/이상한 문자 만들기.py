def solution(s):
    i = j = 0
    res = ''
    while i < len(s):
        if s[i] == ' ':
            res += s[i]
            i += 1
            j = 0
            
        elif j % 2 == 0:
            res += s[i].upper()
            i += 1
            j += 1
        elif j % 2 != 0:
            res += s[i].lower()
            i += 1
            j += 1
    return res