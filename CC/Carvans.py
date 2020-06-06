try:
    for _ in range(int(input())):
        n = int(input())
        p = list(map(int , input().split()))
        c ,z = 0, max(p)
        for i in p:
            if i <= z:
                z = i
                c+=1
        print(c)
except:
    pass