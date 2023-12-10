def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        s,e = parts[i]
        answer += my_strings[i][s:e+1]
    return answer

'''
# join 활용
return ''.join([my_strings[i][parts[i][0]:parts[i][1]+1] for i in range(len(parts))])
'''