try:
    l = int(input())
    b = int(input())
    a = l*b
    p = 2*(l+b)
    if a > p:
        print("Area")
        print(a)
    elif p > a:
        print("Peri")
        print(p)
    else:
        print("Eq")
        print(a)
except:
    pass