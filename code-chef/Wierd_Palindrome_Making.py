try:
    T = int(input())
    while T > 0:
        N = int(input())
        A = list(map(int, input().split()))
        o = [i % 2 != 0 for i in A].count(True)
        if o in [0, 1]:
            print(0)
        else:
            print(o//2)
        T = T - 1
except Exception as e:
    pass


