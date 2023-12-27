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