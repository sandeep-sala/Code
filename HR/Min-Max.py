
def miniMaxSum(arr):
    ar = sorted(arr)
    print(sum(ar[:-1]),sum(ar[1:]))

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    miniMaxSum(arr)
