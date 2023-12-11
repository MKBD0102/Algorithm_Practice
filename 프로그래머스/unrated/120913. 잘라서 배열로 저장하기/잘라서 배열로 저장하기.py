def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0,len(my_str),n)]

# 슬라이싱으로 인덱스 초과 -> 오류 안남