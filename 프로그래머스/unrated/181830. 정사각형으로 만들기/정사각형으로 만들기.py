def solution(arr):
    rows, cols = len(arr), len(arr[0])
    if rows < cols:
        arr.extend([[0]*cols]*(cols-rows))
    elif rows > cols:
        for i in range(rows):
            arr[i].extend([0]*(rows-cols))
    return arr