def solution(A, B):
    for i in range(len(A)):
        if B == A[-i:]+A[:-i]:
            return i
    return -1

'''
# lambda 사용
return lambda A,B : (B*2).find(A)
-> find(A): A가 처음 등장하는 위치 index = 회전 최소 횟수,
만약 A가 없다면 find는 -1을 반환
'''