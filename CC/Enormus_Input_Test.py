try:
    n, k = map( int ,input().split() )
    if (n and k) <= 10**7:
        arr = [ int(input()) for i in range(n)]
        count = 0
        for i in arr:
            if i <= 10**9 and i%k==0:
                count += 1
        print(count)
except:
    pass
