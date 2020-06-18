for _ in range(int(input())):
    p = input()
    if len(p) <= 10:
        print(p)
    else:
        print(p[0]+str(len(p[1:-1]))+p[-1])