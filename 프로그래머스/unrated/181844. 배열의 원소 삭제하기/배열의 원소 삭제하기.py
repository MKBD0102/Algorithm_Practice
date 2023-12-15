def solution(arr, delete_list):
    ans = []
    for n in arr:
        if n not in delete_list:
            ans.append(n)
    return ans

'''
# 리스트 컴프리헨션
return [n for n in arr if n not in delete_list]
'''