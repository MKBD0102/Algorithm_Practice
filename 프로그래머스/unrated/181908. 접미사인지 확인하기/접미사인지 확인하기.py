def solution(my_string, is_suffix):
    if len(my_string) >= len(is_suffix):
        if my_string[-len(is_suffix):] == is_suffix:
            return 1
        else:
            return 0
    else:
        return 0

'''
# 코드 줄이기
return 1 if my_string[-len(is_suffix):] == is_suffix else 0
'''
