def solution(sizes):
    rotated = [[max(size), min(size)] for size in sizes]
    
    max_w = max(size[0] for size in rotated)
    max_h = max(size[1] for size in rotated)
    
    return max_w * max_h

'''
# 모든 명함 회전해서 명함별 긴 모서리는 가로에, 명함별 짧은 모서리는 세로에 배치
# 긴 모서리들 중 가장 긴 모서리가 가로의 최대 길이, 짧은 모서리들 중 가장 긴 모서리가 세로의최대 길이
return max(max(size) for size in sizes)*max(min(size) for size in sizes)
'''
    