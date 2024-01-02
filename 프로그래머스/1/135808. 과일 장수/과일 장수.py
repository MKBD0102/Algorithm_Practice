def solution(k, m, score):
    sorted_score = sorted(score, reverse=True)
    min_scores = sorted_score[m-1::m]
    return sum(map(lambda x: x*m,min_scores))