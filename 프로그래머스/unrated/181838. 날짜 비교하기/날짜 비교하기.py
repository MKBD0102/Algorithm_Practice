def solution(date1, date2):
    if date1[0] < date2[0]:
        return 1
    elif date1[0] == date2[0]:
        if date1[1] < date2[1]:
            return 1
        elif date1[1] == date2[1]:
            if date1[2] < date2[2]:
                return 1
    return 0

'''
# 리스트 -> 각 요소를 순서대로 비교함
def solution(date1, date2):
    return int(date1 < date2)
'''