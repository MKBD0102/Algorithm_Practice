import re

def solution(dartResult):
    pattern = re.compile('(\d+)([SDT])([*#]?)')
    times = pattern.findall(dartResult)
    
    scores = []
    for i, time in enumerate(times):
        
        num, area, option = time
        num = int(num)
        
        if area == "S":
            num = num**1
        elif area == "D":
            num = num**2
        elif area == "T":
            num = num**3
        
        if option == "*":
            if i > 0:
                scores[i-1] = scores[i-1]*2
            num *= 2
        elif option == "#":
            num = -num
        
        scores.append(num)
        
    return sum(scores)

'''
# 조건문 대신 딕셔너리로 SDT 경우와 옵션의 경우를 저장 후 계산
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)
'''