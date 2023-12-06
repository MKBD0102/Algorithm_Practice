def solution(arr, queries):
    for query in queries:
        i,j = query
        num_i = arr[i]
        num_j = arr[j]
        arr[i] = num_j
        arr[j] = num_i
    return arr

'''
def solution(arr, queries):
    for a,b in queries:
    # 값을 따로 저장해두지 않고 바로 교환 가능
        arr[a],arr[b]=arr[b],arr[a]
    return arr

'''