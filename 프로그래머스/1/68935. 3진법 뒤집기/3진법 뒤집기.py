def solution(n):
    
    def dtot(number):
        if number == 0:
            return ''
        else:
            r = number % 3
            return dtot(number // 3) + str(r)
    
    def ttod(string):
        number = 0
        string[::-1]
        for i,s in enumerate(string):
            number += (3 ** i) * int(s)
        return number
    
    return ttod(dtot(n))