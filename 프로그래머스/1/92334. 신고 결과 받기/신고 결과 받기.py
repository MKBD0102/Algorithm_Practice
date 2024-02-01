def solution(id_list, report, k):
    report_set = list(set(report))
    
    cnt = dict.fromkeys(id_list, 0)
    mail = dict.fromkeys(id_list, 0)
    
    for repo in report_set:
        do, get = repo.split(' ')
        cnt[get] += 1
    
    stop = [key for key, value in cnt.items() if value >= k]
    
    for repo in report_set:
        do, get = repo.split(' ')
        if get in stop:
            mail[do] += 1
    
    return list(mail.values())


'''
# 딕셔너리 값 바로 비교
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
'''

