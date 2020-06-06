try:
    for _ in range(int(input())):
        K=sorted([int(x) for x in input().split()])[:3]
        print(K[-2])
except:
    pass