def solution(s):
    return ''.join(sorted([x for x in s if x.islower()],reverse=True)+sorted([x for x in s if x.isupper()],reverse=True))

'''
# 문자열 (오름차순) 정렬 -> 대문자 정렬 후 소문자 정렬
return ''.join(sorted(s,reverse = True))
'''