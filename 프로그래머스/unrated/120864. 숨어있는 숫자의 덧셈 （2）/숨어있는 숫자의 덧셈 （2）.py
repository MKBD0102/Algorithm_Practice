def solution(my_string):
    a = ''.join((' ' if s.isalpha() else s) for s in my_string)
    return sum(int(n) for n in a.split())