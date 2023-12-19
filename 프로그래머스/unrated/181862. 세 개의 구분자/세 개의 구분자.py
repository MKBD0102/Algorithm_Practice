def solution(myStr):
    trans = str.maketrans('abc','   ')
    res = myStr.translate(trans).split()
    return res if res else ["EMPTY"]