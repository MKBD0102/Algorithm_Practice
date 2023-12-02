def solution(dots):
    def gradient(dot1, dot2):
        return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])

    def comb(lst, r):
        res = []
        if r > len(lst):
            return res
        if r == 1:
            for i in lst:
                res.append([i])
        elif r > 1:
            for i in range(len(lst) - r + 1):
                for j in comb(lst[i + 1:], r - 1):
                    res.append([lst[i]] + j)
        return res

    lines = comb(dots, 2)

    for line in lines:
        dots_c = dots.copy()
        for dot in line:
            dots_c.remove(dot)
        grad1 = gradient(line[0],line[1])
        grad2 = gradient(dots_c[0],dots_c[1])

        if grad1 == grad2:
            return 1
    return 0