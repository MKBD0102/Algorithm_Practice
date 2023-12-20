
def solution(i, j, k):
    cnt = 0
    for n in range(i, j+1):
        cnt += str(n).count(str(k))
    return cnt

'''
# 리스트 컴프리헨션 사용
def solution(i, j, k):
    return sum([ str(i).count(str(k)) for i in range(i,j+1)])
'''