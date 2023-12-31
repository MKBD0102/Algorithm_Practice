def solution(s, n):
    low_letter = [chr(x) for x in range(97,123)]
    up_letter = [chr(x) for x in range(65,91)]
    ans = ''
    for a in s:
        if a.islower():
            a = low_letter[(low_letter.index(a) + n) % len(low_letter)]
        elif a.isupper():
            a = up_letter[(up_letter.index(a) + n) % len(up_letter)]
        ans += a
    return ans