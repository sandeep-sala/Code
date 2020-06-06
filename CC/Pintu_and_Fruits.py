try:
    T = int(input())
    for _ in range(T):
        N,M  = list(map(int, input().split()))
        F = list(map(int, input().split()))
        P = list(map(int, input().split()))
        S = {}
        for i in range(N):
            if F[i] not in S:
                S[(F[i])] = (P[i])
            elif F[i] in S:
                S[(F[i])] += (P[i])
        Min = S[list(S.keys())[0]] 
        for key, value in S.items():
            if value < Min:
                Min = value
        print(Min)
except:
    pass