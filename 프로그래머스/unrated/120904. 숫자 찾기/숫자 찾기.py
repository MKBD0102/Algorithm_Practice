def solution(num, k):
    return int(str(num).find(str(k))) + 1 if str(k) in str(num) else -1