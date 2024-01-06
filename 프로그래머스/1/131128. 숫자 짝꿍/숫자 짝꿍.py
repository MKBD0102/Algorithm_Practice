def solution(X, Y):
    X_cnt ={}
    Y_cnt ={}
    
    for x in X:
        if x not in X_cnt.keys():
            X_cnt[x] = 1
        else:
            X_cnt[x] += 1
    for y in Y:
        if y not in Y_cnt.keys():
            Y_cnt[y] = 1
        else:
            Y_cnt[y] += 1
            
    res = ''
    for n in range(10):
        if str(n) in X_cnt.keys() and str(n) in Y_cnt.keys():
            res = str(n) * min(X_cnt[str(n)], Y_cnt[str(n)]) + res
            
    return "-1" if not res else "0" if all(n == "0" for n in res) else res