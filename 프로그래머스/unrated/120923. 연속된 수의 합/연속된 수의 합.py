def solution(num, total):
    return [((total - ((num-1)*(num-2))//2)//num) + i for i in range(num)]