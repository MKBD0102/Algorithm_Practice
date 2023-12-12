def solution(str_list):
    if ("l" not in str_list) and ("r" not in str_list):
        return []
    elif "l" in str_list and "r" not in str_list:
        return str_list[:str_list.index("l")]
    elif "l" not in str_list and "r" in str_list:
        return str_list[str_list.index("r")+1:]
    else:
        if str_list.index("l") < str_list.index("r"):
            return str_list[:str_list.index("l")]
        else:
            return str_list[str_list.index("r")+1:]

'''
# 우선 오는 문자 확인하는 방식
def solution(str_list):
    for s in str_list:
        if s == "l":
            return str_list[:str_list.index("l")]
        elif s == "r":
            return str_list[str_list.index("r")+1:]
    return []
'''