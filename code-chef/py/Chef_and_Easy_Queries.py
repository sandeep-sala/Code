try:
    for _ in range(int(input())):
        n,k=map(int, input().split())
        p = sum( list( map(int,input().split())   ) )
        print(int( (p/k)+1 ))        
except:
    pass