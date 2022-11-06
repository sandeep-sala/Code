from sys import stdin
try:
    for _ in range(int(stdin.readline())):
        n = int(stdin.readline())
        arr = sorted(list(map(int,stdin.readline().split() ))[:n],reverse=True)  
        print(sum([ (arr[j]-j) if (arr[j]-j) >= 0 else 0 for j in range(len(arr))])%1000000007)
except:
    pass
