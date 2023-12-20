def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    elif id_pw[0] in [i for i,_ in db]:
        return 'wrong pw'
    else:
        return 'fail'