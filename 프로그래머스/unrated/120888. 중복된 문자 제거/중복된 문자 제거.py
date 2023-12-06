def solution(my_string):
    return ''.join([k for k in dict.fromkeys(my_string)])