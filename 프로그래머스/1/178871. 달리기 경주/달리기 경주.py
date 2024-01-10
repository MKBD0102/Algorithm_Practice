def solution(players, callings):
    k_v = {}
    v_k = {}
    for i, p in enumerate(players):
        k_v[i] = p
        v_k[p] = i
    
    for c in callings:
        position = v_k[c]
        taken_player = k_v[position - 1]
        
        v_k[c], v_k[taken_player] = position - 1, position
        k_v[position - 1], k_v[position] = c, taken_player
        
    return list(k_v.values())