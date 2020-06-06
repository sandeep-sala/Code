try:
    N = int( input() )
    K=[int(x) for x in input().split()]
    E,O = 0,0
    for k in K:
        if k%2 == 0:
            E+=1
        else:
            O+=1 
    P ="READY FOR BATTLE" if ( E > O ) else "NOT READY"
    print(P)
except:
    pass