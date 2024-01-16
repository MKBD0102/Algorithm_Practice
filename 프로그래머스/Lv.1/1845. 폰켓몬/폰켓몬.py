def solution(nums):
    r = len(nums)//2
    s = len(set(nums))
    
    if r < s:
        return r
    else:
        return s