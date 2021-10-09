try:
    def get_mixture(A,B):
        if ( A>0 and B>0 ):
            return 'Solution'
        if B == 0:
            return 'Solid'
        if A == 0:
            return 'Liquid'

    for _ in range(int(input())):
        A,B = map(int,input().split())
        print(get_mixture(A,B))
except:
    pass