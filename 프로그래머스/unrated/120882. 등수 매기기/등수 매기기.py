def solution(score):
    avg = [(x+y)/2 for x, y in score]
    sorted_avg = sorted(avg, reverse=True)
    return [sorted_avg.index(a)+1 for a in avg]

'''
# dict 활용 (굳이 평균을 다 구할 필요 없이 sum만 해도 비교 가능)
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]
'''