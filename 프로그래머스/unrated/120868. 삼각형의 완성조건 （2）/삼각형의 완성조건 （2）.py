def solution(sides):
    return len(list(range(max(sides) - min(sides)+1,max(sides))) + list(range(max(sides),sum(sides))))