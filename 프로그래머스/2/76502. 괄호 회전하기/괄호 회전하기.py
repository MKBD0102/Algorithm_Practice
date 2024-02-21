def solution(s):
    ln = len(s)
    cnt = 0
    match = {')':'(', '}':'{', ']':'['}
    
    for i in range(ln):
        stack = []
        for j in range(i, i+ln):
            c = s[j%ln]
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if stack and stack[-1] == match[c]:
                    stack.pop()
                else:
                    break
        else:           
            if not stack:
                cnt += 1
    
    return cnt