def solution(nums):
    
    def isprime(n):
        for d in range(2, int(n**(0.5))+1):
            if n % d == 0:
                return False
        return True
    
    cnt = 0
    for i, x in enumerate(nums[:-2]):
        for j, y in enumerate(nums[i+1:-1]):
            for k, z in enumerate(nums[nums.index(y)+1:]):
                hap = x+y+z
                cnt += isprime(hap)
    
    return cnt