def solution(food):
    ans = []
    for i in range(1,len(food)):
        if food[i] // 2 > 0:
            ans += [str(i)] * (food[i] // 2)
    ans = ans+['0']+ans[::-1]
    if len(ans) >= 3:
        return ''.join(ans)