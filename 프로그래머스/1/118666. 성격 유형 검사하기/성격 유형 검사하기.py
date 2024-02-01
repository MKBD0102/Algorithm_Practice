def solution(survey, choices):
    scores = {
        "R":0, "T":0,
        "C":0, "F":0,
        "J":0, "M":0,
        "A":0, "N":0
    }
    
    pair = ["RT","CF","JM","AN"]
    
    for i, c in enumerate(choices):
        if c > 4:
            scores[survey[i][1]] += c - 4
        if c < 4:
            scores[survey[i][0]] += abs(c - 4)
    
    res = ''
    for p in pair:
        if scores[p[0]] > scores[p[1]]:
            res += p[0]
        if scores[p[0]] < scores[p[1]]:
            res += p[1]
        if scores[p[0]] == scores[p[1]]:
            res += min(p[0],p[1])
        
    
    return res