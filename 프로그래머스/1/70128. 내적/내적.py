def solution(a, b):
    return sum(map(lambda x,y: x*y, a,b))

'''
# zip과 리스트 컴프리헨션
return sum([x*y for x,y in zip(a,b)])
'''