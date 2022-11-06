for _ in range(int(input())):
    n = int(input())
    s = input()
    n = s.count("1")
    print( int((n*(n+1))/2) )
