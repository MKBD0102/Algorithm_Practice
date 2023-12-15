def solution(polynomial):
    terms = polynomial.replace(' + ',' ').split()
    x_sum = 0
    c_sum = 0
    for term in terms:
        if term.isdigit():
            c_sum += int(term)
        elif term.replace('x','') == '': 
            x_sum += 1
        else:
            x_sum += int(term.replace('x',''))
    if x_sum == 0:
        return f'{c_sum}'
    elif x_sum == 1:
        return f'x + {c_sum}' if c_sum != 0 else f'x'
    else:
        return f'{x_sum}x + {c_sum}' if c_sum != 0 else f'{x_sum}x'
            