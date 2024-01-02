def solution(food):
    ans = ''
    for i in range(1,len(food)):
        if food[i] // 2 > 0:
            ans += str(i) * (food[i] // 2)
    if len(ans) * 2 + 1 >= 3:
        return ans+'0'+ans[::-1]