try:
    for _ in range(int(input())):
        b = int(input())
        g = 0
        if b < 1500:
            g = b*2
        elif b >= 1500:
            g = b + float(500) + (b*.98)
        print("%.2f" % g)
except:
    pass