def solution(strArr):
    answer = {}
    for s in strArr:
        if len(s) not in answer:
            answer[len(s)] = 1
        else:
            answer[len(s)] += 1
    return max(answer.values())

'''
# get(key, key 없으면 넣을 디폴트 값) (-> key에 해당하는 값) 함수 사용
def solution(strArr):
    answer = {}
    for s in strArr:
        answer[len(s)] = answer.get(len(s),0) + 1
    return max(answer.values())

'''