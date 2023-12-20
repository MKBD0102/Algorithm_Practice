def solution(numlist, n):
    arr = [ [num,abs(num-n)]for num in numlist]
    arr.sort(key = lambda x: (x[1],-x[0]))
    return [ num for num, _ in arr ]