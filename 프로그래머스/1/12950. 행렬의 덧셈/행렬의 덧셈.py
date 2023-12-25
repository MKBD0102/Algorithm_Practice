def solution(arr1, arr2):
    return [[ x+y for x,y in zip(X,Y)] for X,Y in zip(arr1,arr2)]