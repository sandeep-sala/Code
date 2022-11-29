def args_count(*arg,**kwargs):
    return len(arg) + len(kwargs)

print(args_count(100), 1)
print(args_count(100, 2, 3), 3)
print(args_count(32, a1=12), 2)
print(args_count(), 0)