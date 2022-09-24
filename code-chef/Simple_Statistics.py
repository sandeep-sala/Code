try:
    for _ in range(int(input())):
        n,k = map( int,input().split() )
        arr = sorted(list(map(int,input().split() ))[:n])
        if k > 0:
            arr = arr[k:(-1*k)]
        print(  format(sum(arr)/len(arr), '.6f') )
except:
    pass