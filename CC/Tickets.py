try:
    for _ in range(int(input())):
        n = input()
        p = True
        a=n[0]
        b=n[1]
        if a!=b:
            for i in range(len(n)):
                if i%2==0 and n[i]==a:
                    continue
                elif i%2!=0 and n[i]==b:
                    continue
                else:
                    p = False
                    break
        else:
            p=False
        if p == True:
            print("YES")
        else:
            print("NO")
except:
    pass