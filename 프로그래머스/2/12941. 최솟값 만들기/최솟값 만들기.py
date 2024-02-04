def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    return sum(list(map(lambda x: x[0]*x[1], zip(A,B))))