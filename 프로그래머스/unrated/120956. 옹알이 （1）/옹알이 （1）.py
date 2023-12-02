def solution(babbling):
    answer = 0
    for string in babbling:
        for word in ["aya", "ye", "woo", "ma"]:
            if word in string:
                string = string.replace(word,"-")
        if all(s == '-' for s in string):
            answer += 1
    return answer