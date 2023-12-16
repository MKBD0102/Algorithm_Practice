def solution(n_str):
    for i, n in enumerate(n_str):
        if n != '0':
            return ''.join(list(n_str)[i:])
        
'''
# lstrip() -> 왼쪽부터 자르기
return n_str.lstrip('0')
'''