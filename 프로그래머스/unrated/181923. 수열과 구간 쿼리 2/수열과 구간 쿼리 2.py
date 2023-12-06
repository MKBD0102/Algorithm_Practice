def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        lst = [ n for n in arr[s:e+1] if n > k ]
        if len(lst) == 0:
            answer.append(-1)
        else:
            answer.append(min(lst))
    return answer