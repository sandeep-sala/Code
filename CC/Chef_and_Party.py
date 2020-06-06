try:
    for _ in range(int(input())):
        n = int(input())
        arr = sorted(list(map(int,input().split())))
        c = 0
        for i in range(n):
            if arr[0] <= c:
                c += 1
                del arr[0]
            else:
                break
        print(c)
except:
    pass