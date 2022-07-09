try:
    for _ in range(int(input())):
        p = list( input().split() )
        q = list( input().split() )
        c =0
        for i in p:
            if i in q:
                c+=1
        if c>=2:
            print("similar")
        else:
            print("dissimilar")
except:
    pass