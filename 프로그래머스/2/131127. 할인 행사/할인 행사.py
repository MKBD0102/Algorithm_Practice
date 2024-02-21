from collections import Counter

def solution(want, number, discount):
    whish = dict(zip(want, number))
    cnt = 0
    
    for i in range(len(discount)-9):
        membership = discount[i:i+10]
        counts = Counter(membership)
        
        if all(item in counts and counts[item] >= whish[item] for item in whish):
            cnt += 1
    
    return cnt