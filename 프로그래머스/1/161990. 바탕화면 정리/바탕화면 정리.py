def solution(wallpaper):
    lux = 99
    rdx = 0
    luy = 99
    rdy = 0
    for i, row in enumerate(wallpaper):
        if '#' in row:
            luy = min(luy, row.find('#'))
            rdy = max(rdy, row.rfind('#') + 1)
            lux = min(lux, i)
            rdx = max(rdx, i + 1)
    return [lux, luy, rdx, rdy]