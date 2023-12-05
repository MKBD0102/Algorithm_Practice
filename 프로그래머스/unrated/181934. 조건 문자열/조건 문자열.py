def solution(ineq, eq, n, m):
    if eq == "!":
        if ineq == "<":
            return 1 if n < m else 0
        elif ineq == ">":
            return 1 if n > m else 0
    else:
        if ineq == "<":
            return 1 if n <= m else 0
        elif ineq == ">":
            return 1 if n >= m else 0

### eval(): 표현식을 문자열로 받아서 실행
    # return eval(f'1 if {n} {ineq+eq} {m} else 0'.replace('!',''))