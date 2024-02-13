def solution(brown, yellow):
    total = brown + yellow
    
    height = 3
    
    while height <= (yellow + 2):
        width = total // height
        
        if width*height == total and (width - 2)*(height - 2) == yellow:
            return width, height
        
        height += 1
    
    return width, height