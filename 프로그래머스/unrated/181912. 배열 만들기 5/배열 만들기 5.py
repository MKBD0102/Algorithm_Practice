def solution(intStrs, k, s, l):
    ret = []
    for c in intStrs:
        num = int(c[s:s+l])
        if num > k:
            ret.append(num)
    return ret

'''
# 리스트 컴프리헨션
return [int(c[s:s+l]) for c in intStrs if int(c[s:s+l]) > k]
'''