def solution(my_string, overwrite_string, s):
    s_list = list(my_string)
    s_list[s:s+len(overwrite_string)] = list(overwrite_string)
    return ''.join(s_list)