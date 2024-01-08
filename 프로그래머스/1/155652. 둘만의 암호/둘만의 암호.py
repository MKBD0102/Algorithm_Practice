def solution(s, skip, index):
    alphabet_list = [chr(n) for n in range(ord('a'), ord('z') + 1)]
    for r in skip:
        alphabet_list.remove(r)
    ans = ''
    for a in s:
        ans += alphabet_list[(alphabet_list.index(a) + index) % len(alphabet_list)]
    return ans