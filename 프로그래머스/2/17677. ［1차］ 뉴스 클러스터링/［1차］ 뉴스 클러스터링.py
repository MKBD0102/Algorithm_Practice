def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    
    set1 = list()
    set2 = list()
    
    for i in range(len(str1)-1):
        set1.extend({str1[i]+str1[i+1]})
        
    for i in range(len(str2)-1):
        set2.extend({str2[i]+str2[i+1]})
        
    set1 = [i for i in set1 if i.isalpha()]
    set2 = [i for i in set2 if i.isalpha()]
    
    inter = set(set1) & set(set2)
    union = set(set1) | set(set2)
    
    i = 0
    u = 0
    
    for s in inter:
        i += min(set1.count(s), set2.count(s))
    
    for s in union:
        u += max(set1.count(s), set2.count(s))
        
    if i == 0 and u == 0:
        return 1*65536
    else:
        return int(i/u * 65536)