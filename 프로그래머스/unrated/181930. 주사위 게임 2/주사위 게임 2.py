def solution(a, b, c):
    return a+b+c if len(set([a,b,c])) == 3 else (a+b+c)*(a**2+b**2+c**2) if len(set([a,b,c])) == 2 else (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)