def solution(elements):
    l = len(elements)
    elements = elements*2
    cnt = set()
    for i in range(l):
        for j in range(1, l+1):
            hap = sum(elements[i:i+j])
            cnt.add(hap)
    return len(cnt)
