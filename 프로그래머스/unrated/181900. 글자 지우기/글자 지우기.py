def solution(my_string, indices):
    for d in sorted(indices,reverse=True):
        my_string = my_string[:d]+my_string[d+1:]
    return my_string