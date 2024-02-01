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