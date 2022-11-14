
def is_eligible(x, y, a):
    if a >= x and a<y:
        return "YES"
    return "NO"


if __name__ == "__main__":
    for __ in range(  int(input()) ):
        X, Y, A = list(map(int,input().split()))
        print(is_eligible(X, Y, A))