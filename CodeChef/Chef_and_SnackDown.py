try:
    arr = ['2010','2015','2016','2017','2019']
    for __ in range(int(input())):
        n = input()
        if n.strip() in arr:
            print("HOSTED")
        else:
            print("NOT HOSTED")
except:
    pass