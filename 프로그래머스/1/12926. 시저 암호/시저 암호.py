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

'''
# 리스트 생성 X
# 문자도 부등호 비교 가능
def solution(s, n):
    ans = ''
    for a in s:
        if a >= 'a' and a <= 'z':
            ans += chr((ord(a) - ord('a') + n) % 26 + ord('a'))
        elif a >= 'A' and a <= 'Z':
            ans += chr((ord(a) - ord('A') + n) % 26 + ord('A'))
        else:
            ans += a
    return ans
'''