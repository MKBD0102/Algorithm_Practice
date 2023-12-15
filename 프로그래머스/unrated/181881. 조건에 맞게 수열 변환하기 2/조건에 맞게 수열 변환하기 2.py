def solution(arr):
    def phase(n):
        get = []
        res = arr
        for i in range(1,n+1):
            for a in res:
                if a >= 50 and a % 2 == 0:
                    get.append(a//2)
                elif a < 50 and a % 2 == 1:
                    get.append(a*2+1)
                else:
                    get.append(a)
            res = get
            get=[]

        return res
    x = 0
    while x >= 0:
        if set(phase(x)) - set(phase(x+1)) or set(phase(x+1))-set(phase(x)):
            x += 1
        else:
            return x