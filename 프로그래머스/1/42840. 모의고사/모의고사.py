def solution(answers):
    n = 0
    score = []
    while n < 3:
        n += 1
        cnt = 0
        for i, ans in enumerate(answers):
            if n == 1:
                if (i % 5 + 1) == ans:
                    cnt += 1
            if n == 2:
                pattern = [1,3,4,5]
                if i % 2 == 0 and ans == 2:
                    cnt += 1
                elif i % 2 == 1:
                    if pattern[((i - 1) // 2) % 4] == ans:
                        cnt += 1
            if n == 3:
                pattern = [3,1,2,4,5]
                if i % 2 == 0:
                    if pattern[(i // 2) % 5] == ans:
                        cnt += 1
                elif i % 2 == 1:
                    if pattern[((i - 1) // 2) % 5] == ans:
                        cnt += 1
        score.append(cnt)
    print(score)
    print(max(score))
    return [i + 1 for i, s in enumerate(score) if s == max(score)]

'''
# 3가지 pattern & answers index로 비교
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''