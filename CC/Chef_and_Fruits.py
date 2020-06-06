try:
    for _ in range(int(input())):
        a,b,c = map(int,  input().split())
        d = a-b
        if d == 0 :
            print(0)
        else:
            while True:
                if a < b and c >0:
                    a = a+1
                    c = c-1
                if a > b and c >0:
                    b = b+1
                    c = c-1
                if  a - b == 0 or c == 0:
                    print(abs(a-b))
                    break
except:     
    pass