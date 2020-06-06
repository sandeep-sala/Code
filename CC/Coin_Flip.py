try:
    for _ in range(int(input())):
        for __ in range(int(input())):
            I,N,Q = list(map(int , input().split()))
            if ( N%2 == 0 or I == Q):
                print(N//2)
            else:
                print((N//2) + 1)
except:
    pass