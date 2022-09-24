try:
    for _ in range(int(input())):
        n = int(input())
        l = sorted(list(map(int,input().split()))[:n])
        c = l[-1]
        for i in range(1,n):
            if c > l[i] - l[i-1]:
                c = l[i] - l[i-1]
        print(c)
except:
    pass