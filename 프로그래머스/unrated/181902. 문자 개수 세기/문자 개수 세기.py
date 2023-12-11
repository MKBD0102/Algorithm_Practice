def solution(my_string):
    alphabet = [chr(i).upper() for i in range(97,123)] + [chr(i) for i in range(97,123)]
    return [my_string.count(s) for s in alphabet]