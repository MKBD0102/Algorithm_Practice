def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer

'''
# 리스트 컴프리헨션 사용
return ''.join([my_string[i] for i in index_list])
'''