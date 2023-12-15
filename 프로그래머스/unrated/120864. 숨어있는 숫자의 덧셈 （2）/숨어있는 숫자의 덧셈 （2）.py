def solution(my_string):
    a = ''.join((' ' if s.isalpha() else s) for s in my_string).strip()
    return sum(int(n) for n in a.split(' ') if n != '')