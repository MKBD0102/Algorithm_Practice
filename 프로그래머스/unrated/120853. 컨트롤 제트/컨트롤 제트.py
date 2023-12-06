def solution(s):
    strings = s.split(" ")
    i = len(strings)-1
    while i >= 0:
        if strings[i] == 'Z':
            strings = strings[:i-1]+strings[i+1:]
            i -=2
        else:
            i -= 1
    return sum([int(s) for s in strings])