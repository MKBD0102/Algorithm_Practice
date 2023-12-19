def solution(picture, k):
    ans = []
    for string in picture:
        string = ''.join([s*k for s in string])
        ans += [string for i in range(k)]
    return ans

'''
# lambda 함수 사용
return lambda picture, k: [''.join([s*k for s in picture[x//k]]) for x in range(len(picture)*k)]

# for x in range(len(picture)*k) -> 세로로 k배 늘린 만큼 리스트 길이 늘이기
# for s in picture[x//k] -> x는 원래 길이의 k배의 범위를 탐색하므로, 원래 리스트 요소의 인덱스를 찾기 위해 x를 k로 나눈 몫을 찾음.
# ''.join([s*k for s in picture[x//k]]) -> 세로로 k배 늘인 범위를 탐색하는 x, x//k로 인해 같은 원소에 대한 join을 k번 수행하게 됨

'''