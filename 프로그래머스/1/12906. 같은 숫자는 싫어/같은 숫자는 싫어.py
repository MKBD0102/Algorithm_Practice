def solution(arr):
    ans = []
    for n in arr:
        if n not in ans or ans[-1] != n:
            ans.append(n)
    return ans

'''
# in 연산 -> 추가비용 발생 가능
def solution(arr):
    ans = []
    for n in arr:
# 빈 iterable 또는 마지막 원소와 다를 경우 n 추가
        if len(ans) == 0 or ans[-1] != n:
            ans.append(n)

    return ans
'''