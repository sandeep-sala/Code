try:
    for _ in range(int(input())):
        n,k = map( int,input().split() )
        arr = list(map( int,input().split() ) )[:n]
        p = ""
        for i in arr:
            if i <= k:
                k-=i
                p+="1"
            else:
                p+="0"
        print(p)
except:
    pass