try:
    for _ in range(int(input())):
        n = int(input())
        s = input()[:n]
        k = [0,0]
        a = 1 if s[0] == "L" or s[0] == "R" else 0
        for i in s:
            if i == "L" and a == 1:
                k[0] = k[0] - 1
                a = 0
            if i == "R" and a == 1:
                k[0] = k[0] + 1
                a = 0
            if i == "U" and a == 0:
                k[1] = k[1] + 1
                a = 1
            if i == "D" and a == 0:
                k[1] = k[1] - 1
                a = 1
        print(k[0],k[1])
except:
    pass