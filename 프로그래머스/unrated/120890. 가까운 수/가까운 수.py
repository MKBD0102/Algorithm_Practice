def solution(array, n):
    dis = sorted([ abs(i - n) for i in array])
    return n - dis[0] if n - dis[0] in array else n + dis[0]