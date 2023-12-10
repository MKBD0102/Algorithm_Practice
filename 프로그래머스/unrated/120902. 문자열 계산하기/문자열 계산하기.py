def solution(my_string):
    my_string = my_string.replace(" ","")
    my_string = my_string.replace("-","+-")
    nums_list = my_string.split("+")
    return sum([int(n) for n in nums_list])