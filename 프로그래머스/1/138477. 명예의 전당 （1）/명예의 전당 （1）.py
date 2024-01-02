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