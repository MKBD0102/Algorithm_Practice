def solution(keyinput, board):
    res = [0,0]
    for k in keyinput:
        if k == "up" and res[1]+1 <= (board[1]/2):
            res[1] += 1
        elif k == "down" and res[1]-1 >= -(board[1]/2):
            res[1] -= 1
        elif k == "left"and res[0]-1 >= -(board[0]/2):
            res[0] -= 1
        elif k == "right" and res[0]+1 <= (board[0]/2):
            res[0] += 1
        else:
            continue
    return res