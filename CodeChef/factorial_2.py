
def fact(n,k=5,sum=0):
    sum += n//k
    k = k*5
    if n < k:
        return sum
    return fact(n,k,sum)

for _ in range(int(input())):
    N = int(input())
    print(fact(N))