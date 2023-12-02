def solution(board):
    danger = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 1:
                for x in (-1,0,1):
                    for y in (-1,0,1):
                        if -1 < i+x < len(board) and -1 < j+y < len(board):
                            danger.append((i+x,j+y))
    danger = set(danger)
    
    return len(board) ** 2 - len(danger)