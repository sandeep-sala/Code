try:
    for _ in range(int(input())):
        ts = int(input())
        c = 0
        if ts % 2 == 0:
            for i in range(0,ts+1,4):
                if i == 0 :continue
                j,t = i,ts
                while True:
                    j,t = j/2,t/2
                    if j <= 0 or t <= 0: break
                    if j % 2 != 0 and t % 2 != 0:
                        break
                    if j % 2 == 0 and t % 2 != 0:
                        c += 1
                        break
                    if j % 2 == 0 and t % 2 == 0:
                        continue
                    break
        else:
            c = ts//2
        print(c)
except :
    pass