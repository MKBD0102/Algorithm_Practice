def solution(a, b, c, d):
    dices = [a,b,c,d]
    get_num = set(dices)
    if len(get_num) == 1:
        return 1111 * a
    elif len(get_num) == 4:
        return min(dices)
    elif len(get_num) == 3:
        for n in get_num:
            if dices.count(n) == 2:
                get_num.remove(n)
                get_num = list(get_num)
                return get_num[0] * get_num[1]
    elif len(get_num) == 2: 
        for n in get_num:
            if dices.count(n) == 2:
                get_num = list(get_num)
                return (get_num[0] + get_num[1])*abs(get_num[0] - get_num[1])
            elif dices.count(n) == 3:
                get_num.remove(n)
                get_num = list(get_num)
                return (10 * n + get_num[0]) ** 2