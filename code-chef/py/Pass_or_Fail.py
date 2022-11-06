try:
    for _ in range(int(input())):
        n,x,p = map( int, input().split())
        if ((x*3)-(n-x)) >= p:
            print("PASS")
        else:
            print("FAIL")
except:
    pass