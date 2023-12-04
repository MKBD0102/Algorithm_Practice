def solution(emergency):
    em_order = sorted(emergency,reverse=True)
    # em_dict = {k:(em_order.index(k)+1) for k in em_order}
    em_dict = {k:v+1 for v,k in enumerate(em_order)} # index 안쓰는 방법
    return [em_dict.get(k) for k in emergency]