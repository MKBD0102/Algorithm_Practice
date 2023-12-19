def solution(myStr):
    trans = str.maketrans('abc','   ')
    return myStr.translate(trans).split() if myStr.translate(trans).split() else ["EMPTY"]