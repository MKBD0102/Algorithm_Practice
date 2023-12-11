def solution(my_string):
    return ''.join(sorted([s.lower() for s in my_string]))

'''
# string 형식도 sorted() 가능 -> 단 리스트 형식으로 반환
return ''.join(sorted(my_string.lower()))
'''