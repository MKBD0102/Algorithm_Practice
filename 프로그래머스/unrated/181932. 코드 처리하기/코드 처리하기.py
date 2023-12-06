def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = 1
            else:
                if i % 2 ==0:
                    ret += code[i]
        elif mode == 1:
            if code[i] == '1':
                mode = 0
            else:
                if i % 2 != 0:
                    ret += code[i]
            
    return ret if ret != '' else "EMPTY"

'''
# 1 제외 index 2step 반환
ret = code.replace('1','')[::2]
# mode_ for문
for i in range(code.count('1')):
    if mode == 0:
        mode = 1
    else:
        mode = 0
'''