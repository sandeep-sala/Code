def find_outlier(ar):
    o,e = [],[]
    for i in ar:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    return o[0] if len(o) < len(e) else e[0]

print(find_outlier([2, 4, 6, 8, 10, 3]), 3)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)