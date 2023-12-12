def solution(arr):
    idx = []
    for i, n in enumerate(arr):
        if n == 2:
            idx.append(i)
    return arr[min(idx):max(idx)+1] if idx else [-1]

'''
# min, max 안쓰는 방법
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
# index()로 최초의 2의 인덱스 가져오고, arr[::-1].index()로 뒤에서 부터 확인하여 가장 마지막의 2의 인덱스 가져옴
# len(arr) - arr[::-1].index(): arr[::-1]로 인덱스가 뒤집어 졌으므로 리스트 길이에서 빼서 원래 인덱스 찾음
'''