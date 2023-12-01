def solution(num_list):
    def isodd(num):
        return num % 2 != 0
    def iseven(num):
        return num % 2 == 0
    return [ sum(1 for num in num_list if iseven(num)), sum(1 for num in num_list if isodd(num))]