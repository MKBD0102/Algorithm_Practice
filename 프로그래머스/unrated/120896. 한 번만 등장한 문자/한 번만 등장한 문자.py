def solution(s):
    alp = set(s)
    for a in alp:
        if s.count(a) > 1:
            s = s.replace(a,"")
    return ''.join(sorted(s))