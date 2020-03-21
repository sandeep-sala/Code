try:
    for _ in range(int(input())):
        a = int(input())
        g = a
        k = 1
        for i in range(1,a+1):
            for j in range(1,i+1):
                if g > 0:
                    g = g -1
                else:
                    break
            if g>0:
                k = k+1
            else:
                break
        if k > 2:
            k = k-1
        print(k)
except:   
    pass