try:
    for _ in range(int(input())):
        n = int(input())
        s ,sA= 0, 2**n
        if n == 1:
            print(1,1)
            continue
        p = []
        for i in range(1,n):
            p.append(i)
            s += i
            if i == n-1:
                p.append(i)
                s += i
        p.append(sA-s)
        print(*p)
except:
    pass