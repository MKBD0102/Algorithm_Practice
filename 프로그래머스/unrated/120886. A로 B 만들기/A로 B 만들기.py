def solution(before, after):
    for s in before:
        if s in after:
            after = after.replace(s,'',1)
        else:
            return 0
    return 1

'''
# 정렬 후 비교
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0
'''