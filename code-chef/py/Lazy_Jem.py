try:
    for _ in range(int(input())):
        n,b,m = list( map(int,input().split()) )
        k = 0
        while n >0:
            if n%2 == 0:
                k += (n//2)*m
                n = n - (n//2)
            else:
                k += ((n+1)//2)*m
                n = n - ((n+1)//2)
            if n>0:
                k += b
                m = m*2
        print(k)
except:
    pass