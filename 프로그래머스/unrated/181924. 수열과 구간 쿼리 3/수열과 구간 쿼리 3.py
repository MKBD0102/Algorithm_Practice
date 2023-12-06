def solution(arr, queries):
    for query in queries:
        i,j = query
        num_i = arr[i]
        num_j = arr[j]
        arr[i] = num_j
        arr[j] = num_i
    return arr