def delete_nth(order,max_e):
    d,l = {},[]
    if max_e == 0:
        return l
    for i in order:
        if i not in d:
            d[i] = 1
            l.append(i)
        elif d[i] < max_e:
            d[i] += 1
            l.append(i)
    return l

print(delete_nth([20,37,20,21], 1), [20,37,21])
print(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])