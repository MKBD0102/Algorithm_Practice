def solution(binomial):
    a,op,b = binomial.split()
    a = int(a)
    b = int(b)
    return a+b if op == '+' else a-b if op == '-' else a*b