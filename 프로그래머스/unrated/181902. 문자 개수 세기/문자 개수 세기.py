def solution(my_string):
    alphabet = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
    return [my_string.count(s) for s in alphabet]