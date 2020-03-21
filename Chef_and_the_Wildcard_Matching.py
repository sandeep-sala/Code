try:
    for _ in range(int(input())):
        a = str(input())
        b = str(input())
        for i in range(len(a)):
            if a[i] == b[i] or (a[i]=="?" and b[i]!="?") or (a[i]!="?" and b[i]=="?"):
                p = "Yes"
            else:
                p = "No"
                break
        print(p)
except:   
    pass