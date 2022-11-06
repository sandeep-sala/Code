try:
    import math as mt
    for _ in range(int(input())):
        n,m=list(map(int,input().split()))
        print((n*m)//(mt.gcd(n,m)**2 ))
except:
    pass