def solution(myString):
    for s in myString:
        if ord(s) < ord('l'):
            myString = myString.replace(s,'l')
            
    return myString

'''
# translate & maketrans 사용
return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))
'''