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

'''
# 다른 풀이 -> 이동 패턴 -> dict
def solution(park, routes):
    dx = {'N':-1, 'S':1, 'E':0, 'W': 0}
    dy = {'N': 0, 'S':0, 'E':1, 'W':-1}
    
    x, y = -1, -1
    
    H = len(park)
    W = len(park[0])
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x = i
                y = j
                break
        if x != -1:
            break
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        isFalse = False
        for i in range(1, n+1):
            nx, ny = x+dx[op]*i, y+dy[op]*i
            if nx < 0 or ny < 0 or nx > (H-1) or ny > (W-1):
                isFalse = True
                break
            if park[nx][ny] == 'X':
                isFalse = True
                break
        if isFalse:
            continue
        x += dx[op]*n
        y += dy[op]*n
                
    return [x,y]
'''