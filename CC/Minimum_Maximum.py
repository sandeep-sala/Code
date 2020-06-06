try:
    for _ in range(int(input())):
        n = int(input())
        m = min( list( map( int ,input().split() ) )) 
        print(m*(n-1))
except:   
    pass