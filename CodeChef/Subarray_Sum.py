try:
    def SubArraySum(arr, n):
        result = 0
        for i in range(0, n):
            result += (arr[i] * (i+1) * (n-i))
        return result

    for _ in range(int(input())):
        n = int(input())
        s = list(map(int,input().split()))
        print(SubArraySum(s,len(s)))
except:
    pass
