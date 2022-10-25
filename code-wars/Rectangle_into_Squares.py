def sq_in_rect(lng, wdth):
    if lng == wdth:
        return

    p = []
    while lng > 0 and wdth > 0:
        if lng < wdth:
            p.append(lng)
            wdth -= lng
        else:
            p.append(wdth)
            lng -= wdth
    return p


print(sq_in_rect(5, 5), None)
print(sq_in_rect(5, 3), [3, 2, 1, 1])
print(sq_in_rect(3, 5), [3, 2, 1, 1])
print(sq_in_rect(20, 14), [14, 6, 6, 2, 2, 2])
