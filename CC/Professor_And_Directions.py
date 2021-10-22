try:
    for _ in range(int(input())):
        n = int(input())
        s = input()
        if s.count("LL")>0 or  s.count("RR")>0:
            print("YES")
        else:
            print("NO")
except:
    pass