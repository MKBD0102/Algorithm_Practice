def solution(keymap, targets):
    times = {}
    for key in keymap:
        for i, s in enumerate(key):
            if s in times.keys():
                times[s] = min(times[s], i + 1)
            else:
                times[s] = i + 1
    
    res = []
    for target in targets:
        cnt = 0
        for s in target:
            if s in times.keys():
                cnt += times[s]
            else:
                cnt = -1
                break
        
        res.append(cnt)
    return res
            