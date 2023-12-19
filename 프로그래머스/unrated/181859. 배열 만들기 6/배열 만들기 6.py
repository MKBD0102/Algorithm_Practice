def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if stk and stk[-1] == arr[i]:
                stk.pop()
                i += 1
        else:
            stk.append(arr[i])
            i += 1
            
    return stk if stk else [-1]

'''
# while -> 불필요한 i 연산 -> for 문 사용
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
                stk.pop()
        else:
            stk.append(arr[i])
    return stk or [-1]
'''
