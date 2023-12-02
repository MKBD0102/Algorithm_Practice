def solution(array):
    cnt = { k:v for k,v in zip(array,[array.count(n) for n in array]) }
    res = [ k for k, v in cnt.items() if max(cnt.values()) == v ]
    return res[0] if len(res) == 1 else -1