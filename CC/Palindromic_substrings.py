try:
    for _ in range(int(input())):
        n = set( input() )
        k = set( input() )
        p = "No"
        for i in n:
            if i in k:
                p = "Yes"
                break
        print(p)
except:
    pass