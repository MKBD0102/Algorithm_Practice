def solution(my_string, indices):
    for d in sorted(indices,reverse=True):
        my_string = my_string[:d]+my_string[d+1:]
    return my_string

'''
# 리스트 컴프리헨션 사용 & 원본 변경 X
return ''.join([v for i, v in enumerate(my_string) if i not in indices])
'''