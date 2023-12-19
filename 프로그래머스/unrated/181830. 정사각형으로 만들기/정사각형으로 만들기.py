def solution(arr):
    if len(arr) < len(arr[0]):
        arr.extend([[0]*len(arr[0])]*(len(arr[0])-len(arr)))
    elif len(arr) > len(arr[0]):
        for i in range(len(arr)):
            arr[i].extend([0]*(len(arr)-len(arr[i])))
    return arr