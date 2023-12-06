def solution(num_list):
    def prod(lst):
        mul = 1
        for n in lst:
            mul *= n
        return mul
    return 1 if prod(num_list) < sum(num_list)**2 else 0