def solution(a, b):
    dow = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 경과 일수
    days = sum(month_day[:a]) + b - 1 
    idx = days % 7
    
    return dow[idx]