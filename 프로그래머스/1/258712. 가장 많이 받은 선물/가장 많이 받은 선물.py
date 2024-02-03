def solution(friends, gifts):
    give_take = [[0]*len(friends) for _ in friends]
    
    for gift in gifts:
        give, take = gift.split(" ")
        give_take[friends.index(give)][friends.index(take)] += 1
        
    score = [sum(give_take[i]) - sum([give_take[j][i] for j, _ in enumerate(friends) if j != i]) for i, _ in enumerate(friends)]
    
    idx = [i for i in range(len(friends))]
    get = [0]*len(friends)
    for i in idx:
        for j in idx[i+1:]:
            if give_take[i][j] > give_take[j][i]:
                get[i] += 1
            elif give_take[i][j] < give_take[j][i]:
                get[j] += 1
            else:
                if score[i] > score[j]:
                    get[i] += 1
                elif score[i] < score[j]:
                    get[j] += 1
        

    return max(get)