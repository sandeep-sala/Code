try:
    for _ in range(int(input())):
        n = int(input())
        s = list(map(int, input().split()))
        l = []
        c = 1
        if n == 1:
            print(f"{1} {1}")
        else:
            for i in range(n-1):
                if (s[i+1] - s[i]) <= 2:
                    c+=1
                    if i == n -2:
                        l.append(c)
                else:
                    if c > 1  or i == n-2: 
                        l.append(c)
                        if s[i+1] -s[i] > 2 and  i == n-2:
                            l.append(1)
                    else:
                        l.append(1)
                    c = 1
            print(min(l),max(l))
except:
    pass
