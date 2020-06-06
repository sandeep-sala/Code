try:
    for _ in range(int(input())):
        c,d,k = map( int,input().split() )
        if( k % 4 == 0 and k >= d*4 ):
            k -= d*4
            if( k/4 > c or k/4< (c-2*d)) :
                print("no")
            else:
                print("yes") 
        else:
            print("no")
except:
    pass