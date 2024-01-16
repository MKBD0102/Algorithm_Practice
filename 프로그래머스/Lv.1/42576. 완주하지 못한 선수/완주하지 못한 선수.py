def solution(participant, completion):
    freq = {}
    for p in participant:
        freq[p] = freq.get(p, 0) + 1
    
    for c in completion:
        freq[c] -= 1
    
    for k, v in freq.items():
        if v != 0:
            return k