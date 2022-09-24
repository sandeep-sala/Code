try:
    for _ in range(int(input())):
        n = list( map( int, input().split() ) )
        l = len(n)
        n.remove(l-1)
        print(max(n))
except:
    pass