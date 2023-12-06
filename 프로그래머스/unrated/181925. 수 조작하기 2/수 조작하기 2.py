def solution(numLog):
    dic = dict(zip([1,-1,10,-10],['w','s','d','a']))
    return ''.join([dic[numLog[i] - numLog[i-1]] for i in range(1,len(numLog))])