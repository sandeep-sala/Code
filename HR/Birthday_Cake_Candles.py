def birthdayCakeCandles(ar):
    ar = sorted(ar)
    k = ar.count(ar[-1])
    return k

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    print(result)