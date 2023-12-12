def solution(dots):
    [x1, y1], [x2, y2], [x3, y3], [x4, y4] = dots
    l = list(set([x1, x2, x3, x4]))
    h = list(set([y1, y2, y3, y4]))
    return  abs(l[0] - l[1])*abs(h[0] - h[1])

'''
# 집합과 절댓값 함수 사용 안하는 방식
return (max(dots[0]) - min(dots[0])) * (max(dots[1]) - min(dots[1]))
'''