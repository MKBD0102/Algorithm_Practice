def solution(arr1, arr2):
    return [[ x+y for x,y in zip(X,Y)] for X,Y in zip(arr1,arr2)]

'''
# map 함수 활용, * -> 언패킹
def solutin(arr1, arr2):
    return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]

'''