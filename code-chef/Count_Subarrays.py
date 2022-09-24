
# NOT SOLVED
try:
    for _ in range(  int(input()) ):
        s = int(input())
        arr = sorted(list(map(int,input().split()))[:s])
        n_arr = [ [j,i] for j in arr for i in arr ]
        a,m = [],n_arr[0][1]
        for i in n_arr:
            if i[0] <= m:
                m = i[1]
                a.append(i) 
        print(a)
except:
    pass