def solution(picture, k):
    ans = []
    for string in picture:
        string = ''.join([s*k for s in string])
        ans += [string for i in range(k)]
    return ans