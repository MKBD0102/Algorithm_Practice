def solution(board, moves):
    basket = []
    cnt = 0

    for move in moves:
        for h, doll in enumerate(board):
            
            if doll[move-1] != 0:
                if basket and basket[-1] == doll[move-1]:
                    basket.pop()
                    cnt += 2
                else:
                    basket.append(doll[move-1])
                board[h][move-1] = 0
                break
    return cnt            