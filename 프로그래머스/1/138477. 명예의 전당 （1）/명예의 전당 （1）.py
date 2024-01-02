def solution(k, score):
    ans = []
    i = 0
    while i < len(score):
        if i < k:
            ans.append(min(score[:i+1]))
            i += 1
        else:
            sorted_score = sorted(score[:i+1])
            ans.append(min(sorted_score[-k:]))
            i += 1
    return ans

'''
# 슬라이싱 사용 x
def solution(k, score):
    ans = []
    x = []
    for s in score:
        x.append(s)
        x.sort(reverse=True)
        if len(x) > k:
            del x [-1]
        ans.append(min(x))
    return ans
'''