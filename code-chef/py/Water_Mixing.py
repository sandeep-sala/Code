
def perfect_bath(a, b, x, y):
    if a < b:
        if (b-a) <= x:
            return True
    elif a > b:
        if (a-b) <= y:
            return True
    elif a == b:
        return True
    return False


if __name__ == "__main__":
    for __ in range(  int(input()) ):
        A, B, X, Y = list(map(int,input().split()))
        print( "YES" if perfect_bath(A, B, X, Y) else "NO" )