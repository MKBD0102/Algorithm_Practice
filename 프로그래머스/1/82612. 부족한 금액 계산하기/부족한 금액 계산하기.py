def solution(price, money, count):
    shortage = price * sum(range(count+1)) - money
    return shortage if shortage > 0 else 0