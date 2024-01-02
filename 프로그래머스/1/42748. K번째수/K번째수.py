def solution(array, commands):
    ans = []
    for i, j, k in commands:
        sorted_array = sorted(array[i-1:j])
        ans.append(sorted_array[k-1])
    return ans