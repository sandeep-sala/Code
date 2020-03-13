try:
    for _ in range(int(input())):
        K=[int(x) for x in input().split()][:3]
        P ="YES" if ( (K[0]+K[1]+K[2]) == 180 ) else "NO"
        print(P)
except:
    pass