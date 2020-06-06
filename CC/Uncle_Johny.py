try:
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int,input().split()))[:n]
        sl = sorted(l)
        k = int(input())
        print(sl.index(l[k-1])+1)
except:
    pass