def solution(numbers, hand):
    pad = [[1,2,3],
          [4,5,6],
          [7,8,9],
          ["*",0,"#"]]
    
    lx, ly = 3,0
    rx, ry = 3,2
    
    res = ''
    for num in numbers:
        if num != 0:
            nx = (num-1) // 3
        else:
            nx = 3
        ny = pad[nx].index(num)
        
        if ny == 0:
            res += 'L'
            lx, ly = nx, ny
            continue
            
        if ny == 2:
            res += 'R'
            rx, ry = nx, ny
            continue
        
        if ny == 1:
            ld = sum([abs(lx - nx), abs(ly -ny)])
            rd = sum([abs(rx - nx), abs(ry -ny)])
            
            if ld == rd:
                if hand == 'right':
                    res += 'R'
                    rx, ry = nx, ny
                elif hand == 'left':
                    res += 'L'
                    lx, ly = nx, ny

            elif ld > rd:
                res += 'R'
                rx, ry = nx, ny

            elif rd > ld:
                res += 'L'
                lx, ly = nx, ny
            continue
    return res
