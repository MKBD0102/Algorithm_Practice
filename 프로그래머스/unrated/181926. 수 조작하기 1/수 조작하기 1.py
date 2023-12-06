def solution(n, control):
    return n + 1 * control.count('w') - 1 * control.count('s') + 10 * control.count('d') - 10 * control.count('a')

'''
# dictionary 사용 방법
# dict와 zip으로 대응하는 계산 값 저장
dic = dict(zip(['w','s','d','a'],[1,-1,10,-10]))
# dictionary에서 문자열을 순회하며 키에 해당하는 값을 반환, sum 계산
return n + sum([dic[key] for key in control])

# 위 코드로 본인 작성 코드에서 불필요한 반복(찾는 문자마다 매번 문자열 순회) 제거
'''