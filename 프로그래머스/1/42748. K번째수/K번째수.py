def solution(array, commands):
    ans = []
    for i, j, k in commands:
        sorted_array = sorted(array[i-1:j])
        ans.append(sorted_array[k-1])
    return ans

'''
# map 함수 활용
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2]-1], commands))
'''