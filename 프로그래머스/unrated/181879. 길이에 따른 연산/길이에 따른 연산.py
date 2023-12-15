def solution(num_list):
    def mul(lst):
        m = 1
        for n in lst:
            m *= n
        return m
    
    return sum(num_list) if len(num_list) >= 11 else mul(num_list)

'''
# 이전 연산 결과 누적해서 연산하는 함수 reduce()
return sum(num_list) if len(num_list) >= 11 else reduce(lambda x,y: x*y, num_list)
'''