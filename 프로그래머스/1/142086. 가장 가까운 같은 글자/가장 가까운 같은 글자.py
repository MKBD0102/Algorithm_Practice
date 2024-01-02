def solution(s):
    ans = [-1 for _ in range(len(s))]
    for i, x in enumerate(s):
        front = s[:i]
        if x in front:
            rev_front = front[::-1]
            for j, y in enumerate(rev_front):
                if y == x:
                    ans[i] = j+1
                    break
    return ans

'''
# 딕셔너리 활용
def solution(s):
    ans = []
    dic = {}
    for i, a in enumerate(s):
        if a not in dic:
            ans.append(-1)
        else:
            ans.append(i - dic[a])
        dic[a] = i

    return ans
'''