for _ in range(int(input())):
    n,m = map( int, input().split())
    ml = list(map(int,input().split()))
    p = [ i for i in range(1,n+1) if i not in ml ]
    print(*p[::2])
    print(*p[1::2])
