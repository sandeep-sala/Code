try:
    for _ in range(int(input())):
        n=list(map(int,input().split()))
        k = "YES"
        for i in n:
            if n.count(i)%2 != 0:
                k = "NO"
                break
        print(k)
except:
    pass