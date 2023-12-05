def solution(numbers, k):
    if len(numbers) % 2 == 0:
        t = 1
        while t <= k:
            for idx in range(0,len(numbers),2):
                if t == k:
                    return numbers[idx]
                else:
                    t += 1
    else:
        t = 1
        step = 1
        while t <= k:
            if step % 2 == 1:
                for idx in range(0,len(numbers),2):
                    if t == k:
                        return numbers[idx]
                    else:
                        t += 1
                step += 1
            else:
                for idx in range(1,len(numbers),2):
                    if t == k:
                        return numbers[idx]
                    else:
                        t += 1
                step += 1
    
        