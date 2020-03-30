try:
    for _ in range(int(input())):
        n = int(input())
        L = list(map(int, input().split() ))[:n]
        R = list(map(int, input().split() ))[:n]
        P = [L[i]*R[i] for i in range(n)]
        value = 0
        s,k = [],[]
        for index, i in enumerate(P):
            if P.count(i) >1 and i >= max(P):
                s.append(index)
            else:
                value = P.index(max(P)) + 1
        if len(s) > 0:
            for i in s:
                if R.count(R[i]) > 1 and R[i] >= max(R):
                    k.append(i)
                else:
                    value = R.index(max(R))+1
        if len(k) > 0:
            value = k[0]+1
        print(value)     
except:
    pass