try:
    for _ in range(int(input())):
        N,M = map(int,input().split() )
        if N > M:
            print(str(N)+" "+str(N+M))
        else:
            print(str(M)+" "+str(N+M))
except:
    pass