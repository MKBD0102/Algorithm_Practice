def solution(s):
    ln = len(s)
    s_2 = s*2
    cnt = 0
    match = {')':'(', '}':'{', ']':'['}
    
    for i in range(ln):
        stack = []
        for j in s_2[i:i+ln]:
            if not stack:
                stack.append(j)
                continue
            
            if j in '({[':
                stack.append(j)
                continue
                
            if j in ']})' and stack[-1] == match[j]:
                stack.pop()
                continue
            else:
                stack.append(j)
                continue
        if not stack:
            cnt += 1
    
    return cnt