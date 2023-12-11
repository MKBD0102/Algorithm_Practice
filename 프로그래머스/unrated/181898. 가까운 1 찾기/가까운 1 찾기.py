def solution(arr, idx):
    for i in range(idx,len(arr)):
        if arr[i] == 1:
            return i
        elif i == len(arr)-1:
            return -1
        
'''
# 반복문과 조건문 중첩 X -> try except 구문 사용
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)  
                # array.index(x, start, stop) 리스트[start:stop]에서 x의 인덱스 반환
    except:
        answer = -1

    return answer
'''