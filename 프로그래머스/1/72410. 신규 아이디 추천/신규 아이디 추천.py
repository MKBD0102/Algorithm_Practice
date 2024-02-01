def solution(new_id):
    new_id = new_id.lower()
    
    for s in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id = new_id.replace(s,'')
    
    check = new_id
    new_id = ''
    pre = None
    for s in check:
        if pre == '.' and s == '.':
            continue
        else:
            new_id += s
            pre = s
            
    new_id = new_id.strip('.')
    
    if new_id == '':
        new_id += 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    
    if len(new_id) <= 2:
        last = new_id[-1]
        while len(new_id) < 3:
            new_id += last               
        
    return new_id

'''
# 정규식 활용
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st) 
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''