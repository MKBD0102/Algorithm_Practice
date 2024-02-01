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