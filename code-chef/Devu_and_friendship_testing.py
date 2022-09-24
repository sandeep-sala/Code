try:
    for _ in range(int(input())):
        n = int(input())
        P = sorted(list(map(int, input().split() ))[:n])
        c,k = [],0
        for p in P:
            if P.count(p) > 1:
                if p not in c:
                    c.append(p)
            elif P.count(p) == 1:
                k = k+1 
        print( len(c)+k)
except:
    pass