def solution(myString, pat):
    myString = myString.translate({65:'B', 66:'A'})
    return 1 if pat in myString else 0