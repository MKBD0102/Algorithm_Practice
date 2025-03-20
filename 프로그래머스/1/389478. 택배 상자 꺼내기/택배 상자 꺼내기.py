def x(n, w):
    if n // w % 2 == 0:
        return n % w
    else:
        return w - n % w
    
def y(n,w):
    if n % w == 0:
        return n // w
    else:
        return n // w + 1

def solution(n, w, num):
    end_box = [x(n,w), y(n,w)]
    num_box = [x(num,w), y(num,w)]
    
    if end_box[1] % 2 == 0:
        if end_box[0] > num_box[0]:
            ans = end_box[1] - num_box[1]
        else:
            ans = end_box[1] - num_box[1] + 1
    else:
        if end_box[0] < num_box[0]:
            ans = end_box[1] - num_box[1]
        else:
            ans = end_box[1] - num_box[1] + 1
    return ans