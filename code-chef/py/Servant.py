try:
    for _ in range(int(input())):
        K=sorted([int(x) for x in input().split()])[:3]
        P ="What an obedient servant you are!" if (K<10) else "-1"
        print(P)
except:
    pass