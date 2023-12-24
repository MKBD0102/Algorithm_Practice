def solution(arr, divisor):
    ans = [e for e in arr if e % divisor == 0]
    return sorted(ans) if ans else [-1]