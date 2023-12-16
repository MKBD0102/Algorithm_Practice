def solution(myString):
    for s in myString:
        if ord(s) < ord('l'):
            myString = myString.replace(s,'l')
            
    return myString