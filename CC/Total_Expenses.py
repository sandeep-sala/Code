try:
    for _ in range(int(input())):
        [N,M] = map(float,input().split())
        S = N*M if N < 1000 else(  (N*M) -( (N*M)*.10 ) )
        print("%.6f" % S)
except:
    pass