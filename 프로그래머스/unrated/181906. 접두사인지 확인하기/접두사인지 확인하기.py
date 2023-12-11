def solution(my_string, is_prefix):
    l = len(is_prefix)
    return 1 if my_string[:l] == is_prefix else 0