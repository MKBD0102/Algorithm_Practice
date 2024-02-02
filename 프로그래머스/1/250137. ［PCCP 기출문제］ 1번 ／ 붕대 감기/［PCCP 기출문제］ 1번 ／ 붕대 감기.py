def solution(bandage, health, attacks):
    remain = health
    last_time = attacks[-1][0]
    
    now = 0
    s_cnt = 0
    
    t, x, y = bandage
    idx = 0
    
    while now <= last_time:
        if idx < len(attacks) and now == attacks[idx][0]:
            now += 1
            remain = max(0, remain - attacks[idx][1])
            if remain <= 0:
                return -1
            s_cnt = 0
            idx += 1
            continue
        
        s_cnt += 1
        if s_cnt <= t:
            remain = min(health, remain + x)
            
        if s_cnt == t:
            remain = min(health, remain + y)
            s_cnt = 0
        
        now += 1 
        
    return remain