def solution(n):
    def fact(n):
        mul = 1
        for i in range(1,n+1):
            mul *= i
        return mul
    maxi = 0
    for i in range(1,n+1):
        if fact(i) > n:
            return maxi
        elif fact(i) <= n and fact(i) > maxi:
            maxi = i
    return maxi