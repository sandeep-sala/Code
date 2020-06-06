try:
    for _ in range(int(input())):
        p  = str(input())
        d=int(len(p)/2)
        k = True
        if len(p)%2==0:
            for e in p[:d]:
                if p[:d].count(e) !=  p[d:].count(e):
                    k = False
                    break
        else:
            for e in p[:d]:
                if p[:d].count(e) !=  p[d+1:].count(e):
                    k = False
                    break
            pass        
        if k==True:
            print("YES")
        else :
            print("NO")
except:
    pass