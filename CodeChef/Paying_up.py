

for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    l = len(arr)
    print(arr)
    if m in [ sum(arr[i:j]) for i in range(l+1) for j in range(i+1,l+1) ]:
        print("Yes")
    else:
        print("No")