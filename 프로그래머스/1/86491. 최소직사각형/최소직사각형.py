def solution(sizes):
    rotated = [[max(size), min(size)] for size in sizes]
    
    max_w = max(size[0] for size in rotated)
    max_h = max(size[1] for size in rotated)
    
    return max_w * max_h
    