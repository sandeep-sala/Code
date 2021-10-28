try:
    for _ in range(int(input())):
        n, v = map(int, input().split())
        mx,mn = 0,0
        mx = ((n-1)*n)//2
        if(v==1):
            mn = mx
        else:
            if(v>=n-1):
                mn = n - 1
            else:
                mn += v + ( (n-v)*(n-v+1) )//2 - 1
        print(mx,mn)
except:
    pass