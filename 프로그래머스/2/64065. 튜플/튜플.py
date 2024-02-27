def solution(s):
    lst = s.split(',{')
    
    for i, s in enumerate(lst):
        s = s.replace('{','')
        s = s.replace('}','')
        s = list(map(int, s.split(',')))
        lst[i] = s
    
    if len(lst) == 1:
        return lst[0]  
    
    lst = sorted(lst, key=len, reverse=True)
    
    
    reverse = []
    for i, x in enumerate(lst):
        if i < len(lst) - 1:
            reverse.append([n for n in x if n not in lst[i+1]][0])
        if i == len(lst) - 1:
            reverse.append(x[0])
    
    return reverse[::-1]