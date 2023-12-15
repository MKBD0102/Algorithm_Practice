def solution(spell, dic):
    for w in dic:
        if  len(set(spell) - set(list(w))) == 0:    
            return 1
    return 2