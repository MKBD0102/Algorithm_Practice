def solution(name, yearning, photo):
    score = dict(zip(name, yearning))   
    return [sum(score[mem] for mem in members if mem in name) for members in photo]