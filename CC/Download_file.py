try:
    for _ in range(int(input())):
        n,k = map( int,input().split() )
        p =[]
        s = 0
        for _ in range(n):
            t,d = map(int, input().split())
            p.append([t,d])
        i = 0
        while k != 0:  
            if(p[i][0]!= 0):
                k -= 1
                p[i][0] -= 1
            else:
                i += 1
        for i in p:
            if i[0] != 0:
                s += i[0]*i[1] 
        print(s)
except:
    pass