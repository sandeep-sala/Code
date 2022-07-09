try:
    for __ in range(  int(input()) ):
        n,z = map(int, input().split())
        p = []
        for _ in range(n):
            p.append( list( map(int, input().split() ) ) )
        p = [ [(i[0]*i[1]),i[2]] for i in p ]
        a,b = 0,0
        for i in p:
            if(a<=i[0] and i[1]<=z):
                a,b = i[0],i[1]
        if a == 0:
            print('no tablet')
        else:
            print(a)
except:
    pass