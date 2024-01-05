def solution(number, limit, power):
    numlist = [x for x in range(1,number+1)]
    cntlist = []
    for num in numlist:
        i = 1
        cnt = 0
        while i*i <= num:
            if num % i == 0:
                if i*i == num:
                    cnt += 1
                else:
                    cnt += 2
            i += 1
        cntlist.append(cnt)
        
    return sum(x if x <= limit else power for x in cntlist)