try:
    from math import factorial as f
    for _ in range(int(input())):
        N,K=map(int,input().split())
        A=sorted([int(x) for x in input().split()])
        n,r=A.count(A[K-1]),A[:K].count(A[K-1])
        print(f(n)//(f(r)*f(n-r)))
except:
    pass