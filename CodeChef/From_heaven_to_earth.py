try:
    for _ in range(int(input())):
        n,v1,v2=map(int,input().split())
        if ((n*1.414)/v1) > ( (n*2)/v2 ):
            print("Elevator")
        else:
            print("Stairs")
except:
    pass