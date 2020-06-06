def compareTriplets(a,b):
    p,r= 0,0
    for i in range(len(a)):
        if a[i] > b[i]:
            p += 1
        if a[i] < b[i]:
            r += 1
    return str(p)+" "+str(r)

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(result)
