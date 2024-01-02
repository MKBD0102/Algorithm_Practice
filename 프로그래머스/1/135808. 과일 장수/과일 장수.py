def solution(k, m, score):
    sorted_score = sorted(score, reverse=True)
    min_scores = sorted_score[m-1::m]
    return sum(map(lambda x: x*m,min_scores))

'''
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    apple_box = []
    for i in range(0, len(score), m):
        apple_box.append(score[i:i+m])
    for apple in apple_box:
        if len(apple) == m:
            answer += min(apple) * m

    return answer
'''