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
    