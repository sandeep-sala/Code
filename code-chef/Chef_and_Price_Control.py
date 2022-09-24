try:
    for _ in range(int(input())):
       n,k = map(int,input().split())
       arr = map(int, input().split())
       s = 0
       for i in arr:
            if i > k:
               s += abs(i-k)
       print(s)
except:
    pass