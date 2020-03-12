try:
    T = int(input())
    if 1 <= T <= 1000:
        arr = [ list(map(int, input().split())) for i in range(T)]
        no = []
        for i in arr:
            no.append(i[0]+i[1])
        for i in no:
            print(i)
except:
    pass
