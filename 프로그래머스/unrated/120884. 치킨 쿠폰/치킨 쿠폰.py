def solution(chicken):
    total = 0
    servie = 0
    cupon = chicken
    
    while cupon >= 10:
        service = cupon//10
        total += service
        cupon = cupon%10+service
    return total