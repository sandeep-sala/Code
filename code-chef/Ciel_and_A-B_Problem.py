try:
    a,b = map(int,input().split())
    c = a-b
    p = str(c)
    if int(p[-1]) == 9:
        print(p[:-1]+str(int(p[-1]) - 1))
    else:
        print(p[:-1]+str(int(p[-1]) + 1))
except:
    pass