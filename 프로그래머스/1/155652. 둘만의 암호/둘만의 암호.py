def solution(s, skip, index):
    alphabet_list = [chr(n) for n in range(ord('a'), ord('z') + 1)]
    for r in skip:
        alphabet_list.remove(r)
    ans = ''
    for a in s:
        ans += alphabet_list[(alphabet_list.index(a) + index) % len(alphabet_list)]
    return ans

'''
# remove 여러 번 -> 성능 저하
# 처음 리스트 만들 때 skip 제외하고 생성
def solution(s, skip, index):
    alphabet_list = [chr(n) for n in range(ord('a'), ord('z') + 1) if chr(n) not in skip]    
    ans = ''
    for a in s:
        ans += alphabet_list[(alphabet_list.index(a) + index) % len(alphabet_list)]
    return ans
'''