def solution(rank, attendance):
    res = sorted([[r,i] for i, r in enumerate(rank) if attendance[i]],key = lambda x: x[0])
    return 10000*res[0][1]+100*res[1][1]+res[2][1]