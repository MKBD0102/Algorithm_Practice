def solution(s):
    parts = []
    
    while True:
        same = 0
        diff = 0
        
        for i, y in enumerate(s):
            if y == s[0]:
                same += 1
            else:
                diff += 1

            if same == diff:
                s = s[i + 1:]
                parts.append(s[:i+1])
                break
            
            if i == len(s) - 1:
                return len(parts) + 1
        
        if len(s) == 1:
            parts.append(s)
            break
        
        if len(s) == 0:
            break
            
    return len(parts)