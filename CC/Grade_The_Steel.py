try:
    for _ in range(int(input())):
        [h,c,t] = map( float,input().split())
        if h > 50 and c < 0.7 and t > 5600:
            print(10)
        if h > 50 and c < 0.7 and not(t > 5600):
            print(9)
        if not(h > 50) and c < 0.7 and t > 5600:
            print(8)
        if h > 50 and not(c < 0.7) and t > 5600:
            print(7)
        if h > 50 and not c < 0.7 and  not t > 5600:
            print(6)
        if not h > 50 and c < 0.7 and  not t > 5600:
            print(6)
        if not h > 50 and not c < 0.7 and  t > 5600:
            print(6)
        if not h > 50 and not c < 0.7 and  not t > 5600:
            print(5)
except:
    pass