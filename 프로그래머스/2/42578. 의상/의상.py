def solution(clothes):
    closet = {key:[] for _, key in clothes}
    
    for c, key in clothes:
        closet[key].append(c)
    
    for key in closet.keys():
        closet[key] = len(closet[key]) + 1
    
    cnt = 1
    for key, n in closet.items():
        cnt *= n
    return cnt-1

'''
# Counter, reduce 함수 사용
from collections import Counter
from functools import reduce

def solution(clothes):
    counts = Counter([category for _, category in clothes])
    # 의상 종류별로 (의상 개수 + 1)을 곱한 후 모든 의상을 입지 않은 경우인 1을 뺌
    answer = reduce(lambda x, y: x * (y + 1), counts.values(), 1) - 1
    return answer
'''