try:
    a, b = input().split()
    a=int(a)
    b=float(b)
    if 0 < (a and b) <= 2000:
        if(a%5==0  and ((a+0.5) or a)<b):
            b=b-a-0.50
        print('%.2f'%b)
except:
    pass
