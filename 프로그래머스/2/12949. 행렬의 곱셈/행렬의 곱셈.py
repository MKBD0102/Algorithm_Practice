def solution(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    arr2_col_len = len(arr2[0])
    
    res = [[0] * arr2_col_len for _ in range(arr1_len)]

    for i in range(arr1_len):
        for j in range(arr2_col_len):
            for k in range(arr2_len):
                res[i][j] += arr1[i][k] * arr2[k][j]
            
        
    return res