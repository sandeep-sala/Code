try:
    N1 = int( input())
    N2 = int( input())
    if -1000 <= (N1 and N2) <= 1000:
        print( N1-N2 if (N1>N2 ) else N1+N2 )
except:
    pass