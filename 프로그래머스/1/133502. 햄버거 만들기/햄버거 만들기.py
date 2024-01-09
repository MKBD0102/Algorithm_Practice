def solution(ingredient):
    pattern = [1,2,3,1]
    cnt = 0
    tmp = []
    for i, x in enumerate(ingredient):
        tmp.append(x)
        if len(tmp) > 3 and tmp[-4:] == pattern:
            del tmp[-4:]
            cnt += 1
    return cnt