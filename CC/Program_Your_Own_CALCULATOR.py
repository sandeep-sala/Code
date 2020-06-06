try:
    op = {
        "+": (lambda x,y: x+y),
        "-": (lambda x,y: x-y),
        "*": (lambda x,y: x*y),
        "/": (lambda x,y: x/y)
        }
    a = int(input())
    b = int(input())
    o = str(input())
    print(op[o](a,b))
except:
    pass