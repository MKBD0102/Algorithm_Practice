def solution(array, n):
    dis = sorted([ abs(i - n) for i in array])
    return n - dis[0] if n - dis[0] in array else n + dis[0]

'''
def solution(array, n):
# 정렬 기준 key에 람다 식을 넣어서 정렬
# (abs(x-n),x-n) -> 두 번 정렬
# 우선 abs(x-n)으로 가까운 거리의 순서로 수 정렬
# x-n으로 같은 거리에 있는 수들 중 더 작은 순서로 수 정렬
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
'''