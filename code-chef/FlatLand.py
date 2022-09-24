try:
    import math
    for _ in range(int(input())):
        N=int(input())
        S = 0
        while N>0:
            N -= (int(math.sqrt(N))**2)
            S += 1
        print(S)
except:
    pass