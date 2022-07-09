
for __ in range(int(input())):
    N,M  = list(map(int, input().split()))
    P = list(map(int, input().split()))
    for __ in range(M):
        Q = int(input())
        E,O = 0,0
        for p in P:
            if bin(Q^p).count('1')%2 ==0:
                E += 1 
            else:
                O += 1
        print(str(E)+' '+str(O))
