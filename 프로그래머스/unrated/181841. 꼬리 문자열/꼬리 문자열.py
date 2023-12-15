def solution(str_list, ex):
    return ''.join(['' if ex in s else s for s in str_list])