
def diagonalDifference(arr):
    l, r = 0, 0
    le = -1
    for i in range(len(arr)):
        l += arr[i][i]
        r += arr[i][le]
        le -= 1
    return abs(l-r)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
