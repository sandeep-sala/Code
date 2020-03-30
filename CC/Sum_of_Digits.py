try:
    T = int(input())
    if 1 <= T <= 1000:
        N = [ int(input()) for i in range(T)]
        K = []
        for i in N:
            K.append(  sum([int(k) for k in str(i)])  )    
        for T in K:
            if 1 <= T <= 1000000:
                print(T)
except :
    pass
