def solution(num_list):
    def mul(lst):
        m = 1
        for n in lst:
            m *= n
        return m
    
    return sum(num_list) if len(num_list) >= 11 else mul(num_list)