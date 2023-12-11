def solution(array):
    cnt = 0
    for n in array:
        cnt += str(n).count('7')
    return cnt