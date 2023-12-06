def solution(n):
    prime_nums = []
    i = 2
    while i <= n:
        if n % i == 0:
            prime_nums.append(i)
            n = n/i
        else:
            i += 1
    return sorted(list(set(prime_nums)))