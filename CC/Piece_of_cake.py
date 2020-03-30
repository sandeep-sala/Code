try:
    for _ in range(int(input())):
        n = str(input())
        p = []
        c = []
        k="NO"
        for i in n:
            if i not in p:
                p.append(i)
        for j in p: 
            c.append( n.count(j) )
        for q, u in enumerate(p):
            if n.count(u)== sum(c) - c[q] :
                k="YES"
                break
        print(k)
except:
    pass