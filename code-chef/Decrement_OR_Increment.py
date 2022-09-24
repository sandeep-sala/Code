try:
    N = int( input() )
    if 0 <= N <= 1000:
        N += +1 if (N%4 == 0 ) else -1    
        print(N)
except:
    pass