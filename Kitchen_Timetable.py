try:
    for _ in range(int(input())):
        n = int(input())
        l1=list(map(int,input().split()))
        l2=list(map(int,input().split())) 
        c , t= 0, 0
        for i in range(n):
            x = l1[i]-t
            if x >= l2[i]:
                c+=1
            t = l1[i]
        print(c)
except:
    pass