def solution(lottos, win_nums):
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    prize = 0
    unknown = lottos.count(0)
    
    if lottos:
        for num in lottos:
            if num in win_nums:
                prize += 1
                
    return [rank[prize + unknown], rank[prize]]

'''
# 집합 연산 사용
rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}

return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

'''