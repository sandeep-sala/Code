def maps(a):
    return list(map(lambda x: 2*x,a))

print(maps([1, 2, 3]), [2, 4, 6])
print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
print(maps([]), [])