def solution(emergency):
    em_order = sorted(emergency,reverse=True)
    em_dict = {k:(em_order.index(k)+1) for k in em_order}
    return [em_dict.get(k) for k in emergency]