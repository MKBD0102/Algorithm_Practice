def solution(price, money, count):
    shortage = price * sum(range(count+1)) - money
    return shortage if shortage > 0 else 0

'''
# max 함수 사용, count*(count+1)//2: 1부터 count까지의 자연수 합
return max(0,price * count*(count+1)//2 - money)
'''