try:

    def highestPowerof2(n):
        import math

        p = int(math.log(n, 2))
        return int(pow(2, p))

    for _ in range(int(input())):
        n = int(input())
        if n == 0:
            print(1)
        if n in [1,2]:
            print(2)
        else:
            sum = 1
            while(2*sum <= n):
                sum *= 2

                if (sum==n):
                    print(n)
                elif (n == (2*sum -1)):
                    print(n+1)
                else:
                    print(sum)


except Exception as e:
    pass

