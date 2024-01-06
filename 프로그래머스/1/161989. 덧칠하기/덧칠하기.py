def solution(n, m, section):
    done = 0
    cnt = 0
    for s in section:
        if s > done:
            done = s + m - 1
            cnt += 1
    return cnt