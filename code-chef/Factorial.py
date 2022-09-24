try:
    for _ in range(int(input())):
        n = int(input())
        i,c = 1, 0
        while True:
            if ( n // 5**i ) > 0:
                c += ( n // 5**i)
                i += 1
            else:
                break
        print(c)
except:
    pass