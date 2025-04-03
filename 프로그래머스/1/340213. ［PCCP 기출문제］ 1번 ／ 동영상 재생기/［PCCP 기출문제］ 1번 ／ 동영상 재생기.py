def solution(video_len, pos, op_start, op_end, commands):
    def c_prev(pos):
        mm, ss = map(int, pos.split(":"))
        pos = mm * 60 + ss
        
        if pos < 10:
            return "00:00"
        else:
            pos -= 10
            mm = pos // 60
            ss = pos % 60
        
        return f"{mm:02d}:{ss:02d}"
    
    def c_next(pos,end):
        mm, ss = map(int, pos.split(":"))
        pos = mm * 60 + ss
        
        mm, ss = map(int, end.split(":"))
        end = mm * 60 + ss
        
        if end < pos + 10:
            pos = end
        else:
            pos += 10
            mm = pos // 60
            ss = pos % 60
            
        return f"{mm:02d}:{ss:02d}"

    def c_op(pos,s,e):
        pos = int(pos.replace(":", ""))
        s = int(s.replace(":", ""))
        e = int(e.replace(":", ""))
        
        if s <= pos <= e:
            pos = e
        
        return f"{pos//100:02d}:{pos%100:02d}"
        

    for c in commands:
        # 오프닝 구간 확인
        pos = c_op(pos, op_start, op_end)
        
        # 명령어 확인
        if c == "prev":
            pos = c_prev(pos)
            ans = c_op(pos, op_start, op_end)

        elif c == "next":
            pos = c_next(pos, video_len)
            ans = c_op(pos, op_start, op_end)
        
    return ans