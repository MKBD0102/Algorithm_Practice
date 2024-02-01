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

'''
# dict 사용하지 않는 방법
def solution(survey, choices):
    answer = ''
    RTCFJMAN = [0,0,0,0,0,0,0,0]
    str = "RTCFJMAN"
    for i in range(len(survey)):
        RTCFJMAN[str.index(survey[i][1])] += choices[i]-4

    if(RTCFJMAN[0]>=RTCFJMAN[1]): answer+= "R"
    else: answer+="T"
    if(RTCFJMAN[2]>=RTCFJMAN[3]): answer+= "C"
    else: answer+="F"
    if(RTCFJMAN[4]>=RTCFJMAN[5]): answer+= "J"
    else: answer+="M"
    if(RTCFJMAN[6]>=RTCFJMAN[7]): answer+= "A"
    else: answer+="N"


    return answer
'''