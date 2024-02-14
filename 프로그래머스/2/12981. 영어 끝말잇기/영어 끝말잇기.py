def solution(n, words):
    cnt = [0]*n
    idx = 0
    for i, word in enumerate(words):
        idx = i % n
        cnt[idx] += 1
        
        if word in words[:i] or (i > 0 and word[0] != words[i-1][-1]):
            return [idx+1, cnt[idx]]
    
    return [0,0]