try:
    for _ in range(int(input())):
        N,K=map(int,input().split())
        P = 'YES' if ( (N*K)%2==0 ) else 'NO'
        print(P)
except:
    pass