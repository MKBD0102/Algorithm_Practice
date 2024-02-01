def solution(data, ext, val_ext, sort_by):
    idx = {"code":0,"date":1, "maximum":2, "remain":3}
    
    data_ext = [ x for x in data if x[idx[ext]] < val_ext]
    data_ext.sort(key=lambda x:x[idx[sort_by]])
    
    return data_ext