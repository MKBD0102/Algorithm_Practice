def solution(arr):
    res = []
    for n in arr:
        get = [n for i in range(n)]
        res = res+get
    return res

'''
# 리스트 컴프리헨션
return [n for n in arr for i in range(n)]
'''