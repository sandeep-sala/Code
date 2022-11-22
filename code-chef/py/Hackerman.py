
def is_prime(x,y):
    n = int(x+y)
    p = True
    for i in range(2,n):
        if n % i == 0:
            p = False
    return p


if __name__ == "__main__":
    for __ in range(  int(input()) ):
        X, Y = list(map(int,input().split()))
        print( "Alice" if is_prime(X, Y) else "Bob" )