def solution(numbers, direction):
    if direction == 'left':
        first = numbers[0]
        for i in range(len(numbers)-1):
            numbers[i] = numbers[i+1]
        numbers[-1] = first
    else:
        end = numbers[-1]
        for i in range(len(numbers)-1,0,-1):
            numbers[i] = numbers[i-1]
        numbers[0] = end
    return numbers