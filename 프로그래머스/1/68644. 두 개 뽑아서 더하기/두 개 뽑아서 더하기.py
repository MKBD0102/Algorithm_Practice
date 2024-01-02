def solution(numbers):
    return sorted({x+y for i, x in enumerate(numbers[:-1]) for j, y in enumerate(numbers[i+1:])})