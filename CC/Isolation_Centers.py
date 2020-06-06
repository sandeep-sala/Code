try:
    for _ in range(int(input())):
        n,k = map(int, input().split())
        s = input()
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1
        for _ in range(k):
            p = int(input())
            q = [ i-p for i in d.values() if i > p ]
            print(sum(q))
except:
    pass