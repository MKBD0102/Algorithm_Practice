def solution(before, after):
    for s in before:
        if s in after:
            after = after.replace(s,'',1)
        else:
            return 0
    return 1
    