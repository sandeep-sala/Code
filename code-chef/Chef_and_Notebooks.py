ans = ["LuckyChef","UnluckyChef"]
for _ in range(int(input())):
    O = []
    X,Y,K,N = map(int, input().split())
    O = [ list(map(int, input().split())) for i in range(N) ]
    p_left = X - Y
    if p_left <= 0:
        print(ans[0])
    else:
        if(any([ 1 if i>=p_left and j<=K else 0 for i,j in O ])):
            print(ans[0])
        else:
            print(ans[1])
    