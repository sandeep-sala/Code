try:
    for _ in range(int(input())):
        n = int(input())
        S = list(map(str,input().split()))[:n]
        n = int(input())
        s = list(map(str,input().split()))[:n]
        for i in s:
            if i in S:
                k = "Yes"
            else:
                k = "No"
                break
        print(k) 
except:
    pass