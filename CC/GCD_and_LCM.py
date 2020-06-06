try:
    import math
    for _ in range(int(input())):
        s=list(map(int,input().split()))
        g=math.gcd(s[0],s[1])
        l=int(s[0]*s[1]/g)
        print(g ,l)
except:
    pass