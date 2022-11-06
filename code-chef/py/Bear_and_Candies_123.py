try:
    for _ in range(int(input())):
        l,b = map(int,input().split())
        t = 0
        p = 1
        while True:
            if t == 0:
                if  p<=l: 
                    l = l-p
                    t=1
                else:
                    print("Bob")
                    break
            else:
                if p<=b:
                    b = b-p
                    t=0
                else:
                    print("Limak")
                    break
            p = p+1
except:
    pass