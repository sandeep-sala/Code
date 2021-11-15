def total_inc_dec(x):
    n = 1
    for i in range(1,10):
        n = n*(x+i)//i
    return n*(20+x)//10-10*x-1

total_inc_dec(23)