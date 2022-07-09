try:
    p1,p2,A,B = 0 , 0,0,0
    for _ in range(int(input())):
        N,M  = list(map(int, input().split()))
        p1 += N
        p2 += M
        D = abs(p1-p2)
        if p1 > p2 and A < D:
            A = D
        elif p1 < p2 and B < D:
            B = D
    if A > B:
        print("1",A)
    else:
        print("2",B)        
except:
    pass