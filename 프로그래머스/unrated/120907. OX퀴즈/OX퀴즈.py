def solution(quiz):
    answer = []
    for s in quiz:
        qa = s.split(" = ")
        qa[0] = qa[0].replace("- -","+ ")
        qa[0] = [ int(n) for n in qa[0].replace("- ", "+ -").split(" + ")]
        if sum(qa[0]) == int(qa[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer