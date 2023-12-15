def solution(arr, k):
    return list(map(lambda x:x*k,arr)) if k % 2 == 1 else list(map(lambda x:x+k,arr))

'''
# 리스트 컴프리헨션
return [n * k if k % 2 == 1 else n + k for n in arr]
'''