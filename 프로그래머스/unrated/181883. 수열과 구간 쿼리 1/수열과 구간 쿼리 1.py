def solution(arr, queries):
    for s, e in queries:
        for i in range(s,e+1):
            arr[i] += 1
    return arr


'''
# enumerate -> index와 value 한 번에

for s, e in queries:
        arr = [n+1 if s <= i <= e else n for i, n in enumerate(arr)]
return arr
'''