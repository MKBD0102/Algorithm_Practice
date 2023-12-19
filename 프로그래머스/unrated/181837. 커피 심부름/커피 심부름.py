def solution(order):
    total = 0
    for m in order:
        if 'americano' in m or 'anything' in m:
            total += 4500
        elif 'cafelatte' in m:
            total += 5000
    return total