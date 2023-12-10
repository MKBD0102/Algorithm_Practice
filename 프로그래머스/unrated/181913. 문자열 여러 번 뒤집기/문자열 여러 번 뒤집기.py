def solution(my_string, queries):
    my_string = list(my_string)
    for i, j in queries:
        if i == 0:
            my_string[i:j+1] = my_string[j::-1]
        else:
            my_string[i:j+1] = my_string[j:i-1:-1]
    return ''.join(my_string)

'''
# 조건문 안쓰고
def solution(my_string, queries):
    my_string = list(my_string)
    for i, j in queries:
        my_string[i:j+1] = my_string[i:j+1][::-1]
    return ''.join(my_string)
'''