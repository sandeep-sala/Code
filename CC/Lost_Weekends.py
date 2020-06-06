try:
    for __ in range(int(input())):
        p = list(map( int, input().split() ))
        p = sum(list(map(lambda x:x*p[-1] , p[:-1])))
        if p <= 120:
            print("NO")
        else:
            print("YES")
except:
    pass