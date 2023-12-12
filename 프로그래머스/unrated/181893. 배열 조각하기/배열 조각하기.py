def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr

'''
# 인덱스 색인 과정 제외
def solution(arr, query):
    for i, n in enumerate(query):
        if i % 2 == 0:
            arr = arr[:j+1]
        else:
            arr = arr[j:]
    return arr
'''