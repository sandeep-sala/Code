try:
    for _ in range(int(input())):
        n = int(input())
        p = True
        for i in range(2,n):
            if n % i == 0:
                p = False    
        if p == True:
            print("yes")
        else:
            print("no")
except:
    pass