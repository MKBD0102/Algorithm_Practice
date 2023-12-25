def solution(s):
    return ''.join(sorted([x for x in s if x.islower()],reverse=True)+sorted([x for x in s if x.isupper()],reverse=True))