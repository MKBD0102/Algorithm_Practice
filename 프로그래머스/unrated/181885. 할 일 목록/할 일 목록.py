def solution(todo_list, finished):
    return [todo_list[i] for i in range(len(finished)) if not finished[i]]

'''
# enumerate 사용
return [s for i,s in enumerate(todo_list) if not finished[i]]
'''