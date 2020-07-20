try:
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int,input().split()))
        a , c = l[0], 0
        for i in l[1:]:
            c += (abs(i - a)) - 1
            a = i
        print(c)
except:
    pass
