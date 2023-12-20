def solution(score):
    avg = [(x+y)/2 for x, y in score]
    sorted_avg = sorted(avg, reverse=True)
    return [sorted_avg.index(a)+1 for a in avg]