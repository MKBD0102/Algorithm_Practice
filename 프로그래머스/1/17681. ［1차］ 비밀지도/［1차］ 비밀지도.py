def solution(n, arr1, arr2):
    def bin_num(n, l):
        res = ''
        while n != 0:
            d = n % 2
            n = n // 2
            res = str(d) + res
        return res.zfill(l)
    
    map_fin = []
    for i in range(n):
        map1_row = bin_num(arr1[i],n)
        map2_row = bin_num(arr2[i],n)
        
        row = ''
        for j in range(n):
            if map1_row[j] == '1' or map2_row[j] == '1':
                row += '#'
            else:
                row += ' '
        map_fin.append(row)
    return map_fin