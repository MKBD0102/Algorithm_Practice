def solution(s):
    alp = set(s)
    for a in alp:
        if s.count(a) > 1:
            s = s.replace(a,"")
    return ''.join(sorted(s))

'''
# 리스트 컴프리헨션
return ''.join(sorted([a for a in set(s) if s.count(a) == 1]))
'''