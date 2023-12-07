def solution(n):
    collatz = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            collatz.append(n)
        else:
            n = 3 * n +1
            collatz.append(n)
            
    return collatz