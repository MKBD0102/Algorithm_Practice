def solution(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append('(')
        if x == ')':
            if not stack:
                return False
            stack.pop()
        
    return not stack
    
    