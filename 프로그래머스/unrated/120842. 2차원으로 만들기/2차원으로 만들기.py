def solution(num_list, n):
    row = []
    for i in range(0,len(num_list)-n+1,n):
        col = []
        for j in range(n):
            col.append(num_list[i+j])
        row.append(col)
    return row