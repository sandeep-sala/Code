
def is_more_time_complexity(x,y):
    return 'Yes' if x > y else 'No'


if __name__ == "__main__":
    for __ in range(  int(input()) ):
        X, Y = list(map(int,input().split()))
        print(is_more_time_complexity(X, Y))