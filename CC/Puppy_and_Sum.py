try:
    for _ in range(int(input())):
        d,n = list(map(int,input().split()))
        s = 0
        for _ in range(1,d+1):
            s = sum([ i for i in range(1,n+1)])
            n = s
        print(s)
except:
    pass