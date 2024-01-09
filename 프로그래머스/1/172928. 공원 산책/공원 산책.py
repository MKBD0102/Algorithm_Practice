def solution(park, routes):
    for i, row in enumerate(park):
        if 'S' in row:
            res = [i, row.find('S')]
            break
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        if op == 'N':
            if res[0] - n < 0:
                pass
            elif 'X' in [x[res[1]] for x in park[res[0]-n:res[0]]]:
                pass
            else:
                res[0] -= n
        
        if op == 'S':
            if res[0] + n >= len(park):
                pass
            elif 'X' in [x[res[1]] for x in park[res[0]:res[0]+n+1]]:
                pass
            else:
                res[0] += n
        
        if op == 'W':
            if res[1] - n < 0:
                pass
            elif 'X' in park[res[0]][res[1]-n:res[1]]:
                pass
            else:
                res[1] -= n
                
        if op == 'E':
            if res[1] + n >= len(park[0]):
                pass
            elif 'X' in park[res[0]][res[1]:res[1]+n+1]:
                pass
            else:
                res[1] += n
                
    return res