def solution(n):
    
    def dtot(number):
        if number == 0:
            return ''
        else:
            r = number % 3
            return dtot(number // 3) + str(r)
    
    def ttod(string):
        number = 0
        reversed(string)
        for i,s in enumerate(string):
            number += (3 ** i) * int(s)
        return number
    
    return ttod(dtot(n))

'''
# 재귀 함수 사용 X, 문자열 뒤집기 X
def solution(n):
    ternay = []
    answer = 0
    power = 0
    
    while n > 0:
        ternay.append(n % 3)
        n = n // 3
    
    for i in reversed(ternay):
        answer += i * (3 ** power)
        power += 1
    
    return answer
'''
