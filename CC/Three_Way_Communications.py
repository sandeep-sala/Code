try:
    from math import sqrt
    for _ in range(int(input())):
        r = int(input())
        [a1,a2] = map(int,  input().split())
        [b1,b2] = map(int,  input().split())
        [c1,c2] = map(int,  input().split())
        d1=sqrt( (b1-a1)**2+(b2-a2)**2 )
        d2=sqrt( (c1-b1)**2+(c2-b2)**2 )
        d3=sqrt( (c1-a1)**2+(c2-a2)**2 )
        if d1<=r and d2<=r or d2<=r and d3<=r or d3<=r and d1<=r:
            print("yes")
        else:
            print("no")
except:    
    pass