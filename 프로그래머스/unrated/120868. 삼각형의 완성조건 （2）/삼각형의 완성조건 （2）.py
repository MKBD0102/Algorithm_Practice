def solution(sides):
    return len(list(range(max(sides) - min(sides)+1,max(sides))) + list(range(max(sides),sum(sides))))

'''
# # 가장 길지 않을 조건: max(sides) < res < sum(sides)
# # 구간 길이 = 만족하는 정수 개수
# sum(sides) - max(sides) - 1

# # 가장 길 조건: max(sides) - min(sides) < res < max(sides)
# max(sides) - max(sides) + min(sides) - 1
# -> min(sides) - 1

# # 가능한 총 정수 개수
# sum(sides) - max(sides) - 2 + min(sides)

# 따라서
return sum(sides) - max(sides) + min(sides) - 2
'''
