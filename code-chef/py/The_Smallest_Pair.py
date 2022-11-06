try:
    for _ in range(int(input())):
        n = int(input())
        s = sorted(list(map(int,input().split()))[:n])
        print(s[0]+s[1])
except:
    pass