try:
    R =[6,2,5,5,4,5,6,3,7,6]
    for _ in range(int(input())):
        N,K=map(int,input().split())
        SUM = 0
        for i in str( N+K ):
            SUM += R[int(i)]
        print(SUM)
except:
    pass