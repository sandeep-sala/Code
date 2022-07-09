try:
    E = [2, 4, 6, 8, 10, 12, 14, 16]
    O = [1, 3, 5, 7, 9, 11, 13, 15]
    for _ in range(int(input())):
        A,B,P,Q = map(int, input().split())
        if (A==P and B==Q):
            print(0)
            continue
        X = (A+B)
        Y = (P+Q)
        if (X in E and Y in E) or (X in O and Y in O):
            print(2)
        else:
            print(1)
except:
    pass
