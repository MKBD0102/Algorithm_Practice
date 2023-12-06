def solution(l, r):
    answer = []
    for n in range(l,r+1):
        if n % 5 == 0:
            if len(set([int(s) for s in str(n)]) - set([0,5])) == 0:
                answer.append(n)
        
    return [-1] if answer == [] else answer