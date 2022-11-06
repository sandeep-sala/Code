def mygcd(x, y):
    return mygcd(y%x, x) if x != 0 else y



print(mygcd(30,12),6)
print(mygcd(8,9),1)
print(mygcd(1,1),1)