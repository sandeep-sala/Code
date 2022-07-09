try:
    for _ in range(int(input())):
        N,D = map(int,input().split())
        n = N
        r,a,c = 0, 0, 0
        while(n > 0):
            r = n % 10
            n = n // 10
            c += 1

            if( r == D ):
                n = n * pow(10,c) + (r+1)*pow(10,c-1)
                a = n - N
                c = 0
        print(a) 
except Exception as e:
    pass

