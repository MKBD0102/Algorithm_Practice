def solution(n):
    for i in range(1,n+1):
        if i ** 2 == n:
            answer = 1
            break
        else:
            answer = 2
    return answer