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