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
            
'''
# 시간 복잡도는 같음
# 중복되는 코드 없는 풀이
def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        answer=1111*a
    elif a==b==c:
        answer=(10*a+d)**2
    elif a==b==d:
        answer=(10*a+c)**2
    elif a==c==d: 
        answer=(10*a+b)**2
    elif b==c==d:
        answer=(10*d+a)**2
    elif a==b and c==d:
        answer=(a+c)*abs(a-c)
    elif a==c and b==d:
        answer=(a+b)*abs(a-b)
    elif a==d and b==c:
        answer=(a+b)*abs(a-b)
    elif a==b:
        answer=c*d
    elif a==c:
        answer=b*d
    elif a==d:
        answer=b*c
    elif b==c:
        answer=a*d
    elif b==d:
        answer=a*c
    elif c==d:
        answer=a*b
    else:
        answer=min(a,b,c,d)

    return answer
'''