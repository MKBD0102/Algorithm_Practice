def solution(arr):
    i = 1
    lcm = arr[0]
    while i < len(arr):
        for n in range(max(lcm,arr[i]),(lcm*arr[i]+1)):
            if n % lcm == 0 and n % arr[i] == 0:
                lcm = n
                break
        i += 1
        
    return lcm