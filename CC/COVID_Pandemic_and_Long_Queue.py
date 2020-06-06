try:
    for _ in range(int(input())):
        n = int(input())
        arr = input().replace(" ","")[:n]
        flag = 0
        if arr.count("1") == 1:
            flag = 1
        else:
            for i in range(n):
                if arr[i] == "1":
                    try:
                        if arr[i+1:i+6].count("1") == 0:
                            flag = 1
                        else:
                            flag = 0
                            break
                    except:
                        if i != n-1:
                            flag = 0
                            break
        if flag == 0:
            print("NO")
        else:
            print("YES")
except:
    pass
