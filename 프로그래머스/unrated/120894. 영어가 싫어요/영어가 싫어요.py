def solution(numbers):
    code = dict(zip([ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],['0','1','2','3','4','5','6','7','8','9']))
    
    for old,new in code.items():
        numbers = numbers.replace(old,new)
        
    return int(numbers)