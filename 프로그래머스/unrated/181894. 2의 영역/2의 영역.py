def solution(arr):
    idx = []
    for i, n in enumerate(arr):
        if n == 2:
            idx.append(i)
    return arr[min(idx):max(idx)+1] if idx else [-1]