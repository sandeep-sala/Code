try:
    for _ in range(int(input())):
        m,n = map(int, input().split())
        w = input().split()
        l ,ll= [],[]
        for _ in range(n):
            n1 = (input().split())
            l.extend(n1[1:])
        for i in w:
            if i in l:
                ll.append("YES")
            else:
                ll.append("NO")
        print(" ".join(ll))
except:
    pass