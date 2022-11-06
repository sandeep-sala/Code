try:
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        c = []
        f = True
        for i in arr:
            if i == 5:
                c.append(5)
            elif i == 10:
                if c.count(5) > 0:
                    c.append(10)
                    c.remove(5)
                else:
                    f = False
                    break
            elif i == 15:
                if(c.count(10) > 0):
                    c.remove(10)
                    c.append(15)
                elif(c.count(10) == 0 and c.count(5) >= 2):
                    c.remove(5)
                    c.remove(5)
                    c.append(15)
                else:
                    f = False
                    break
        if f:
            print("YES")
        else:
            print("NO")
except:
    pass
