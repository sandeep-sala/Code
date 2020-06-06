try:
    for _ in range(int(input())):
        n=int(input())
        p = []
        for _ in range(n):
            p.append(int(input()))
        for i in p:
            if p.count(i) % 2 != 0:
                print(i)
                break
except:
    pass