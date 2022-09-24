def each_cons(lst, n):
    return [ lst[i:i+n]  for i in range(len(lst)+1) if len(lst[i:i+n])==n ]


print(each_cons([3, 5, 8, 13], 2), [[3,5], [5,8], [8,13]])