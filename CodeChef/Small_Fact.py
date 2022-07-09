try:
    def fact(n):
        return n*fact(n-1) if(n>1) else 1
    for x in range( int(input()) ):
        print( fact( int( input() ) ) )
except:
    pass
