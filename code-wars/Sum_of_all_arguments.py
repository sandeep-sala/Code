def sum_args(*args):
    return sum(args)


print( sum_args(1), 1 )
print( sum_args(1, 2), 3 )
print( sum_args(5, 7, 9), 21 )
print( sum_args(12, 1, 1, 1, 1), 16 )
print( sum_args(12, 1, 1, 1, 1, 1, 1), 18 )