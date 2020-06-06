def divisibleSumPairs(n, k, ar):
    c= 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                c+=1
    return c


print(divisibleSumPairs(6, 3, [1,3,2,6,1,2])) 