def solution(numbers):
    answer = 0
    for i in range( len(numbers) ):
        for j in range( i + 1, len(numbers) ):
            pro = numbers[i] * numbers[j]
            if pro > answer:
                answer = pro
    return answer