try:
    for _ in range(int(input())):
        n,k= map(int, input().split())
        p = list(map(int,input().split()))[:n]
        l = list(map(lambda x: (x+k)%7, p) )
        print(l.count(0))
except:
    pass