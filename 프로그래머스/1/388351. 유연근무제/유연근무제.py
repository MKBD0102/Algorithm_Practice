def solution(schedules, timelogs, startday):
    # num_people
    n = len(schedules)
    
    # deadline
    deadline = [x+10 if (x+10) % 100 < 60 else (x//100+1)*100+((x+10)%100-60) for x in schedules]
    
    # event day
    event_day = [startday + i if startday+i < 8 else startday + i - 7 for i in range(7)]
    
    # scores
    scores = [[0]*7 for _ in range(n)]
    for i in range(n):
        for j in range(7):
            if timelogs[i][j] <= deadline[i] and event_day[j] < 6:
                scores[i][j] = 1
    
    # total
    total = [sum(lst) for lst in scores]
    
    return total.count(5)