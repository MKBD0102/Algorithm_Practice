def solution(n_str):
    for i, n in enumerate(n_str):
        if n != '0':
            return ''.join(list(n_str)[i:])