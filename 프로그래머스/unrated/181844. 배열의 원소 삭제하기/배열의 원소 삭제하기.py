def solution(arr, delete_list):
    ans = []
    for n in arr:
        if n not in delete_list:
            ans.append(n)
    return ans