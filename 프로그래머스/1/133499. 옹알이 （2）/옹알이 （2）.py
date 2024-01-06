def solution(babbling):
    cnt = 0
    replace_dict = {'aya':' ','ye':' ','woo':' ','ma':' '}
    for s in babbling:
        copy = s
        for k,v in replace_dict.items():
            if k*2 not in s:
                copy = copy.replace(k,v)
        if not copy.split():
            cnt += 1
    return cnt