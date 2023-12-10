def solution(intStrs, k, s, l):
    ret = []
    for c in intStrs:
        num = int(c[s:s+l])
        if num > k:
            ret.append(num)
    return ret