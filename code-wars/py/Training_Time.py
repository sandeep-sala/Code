def shuffle_it(a, *args):
    for i in args:
        a[i[0]], a[i[1]] = a[i[1]], a[i[0]]
    return a


print(shuffle_it([1,2,3,4,5],[1,2]), [1,3,2,4,5])
print(shuffle_it([1,2,3,4,5],[1,2],[3,4]), [1,3,2,5,4])
print(shuffle_it([1,2,3,4,5],[1,2],[3,4],[2,3]), [1,3,5,2,4])
print(shuffle_it([1,2,3,4,5],[4,4]), [1,2,3,4,5])
print(shuffle_it([1,2,3,4,5]), [1,2,3,4,5])