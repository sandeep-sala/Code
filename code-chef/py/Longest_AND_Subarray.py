try:

    def highestPowerof2(n):
        import math

        p = int(math.log(n, 2))
        return [int(pow(2, p)),int(pow(2, p+1))]

    def get_mex_or(n):
        if n == 0:
            return 1
        elif n in [1,2]:
            return 2
        
        s, l = highestPowerof2(n)

        if n == l-1:
            return n+1
        else:
            return s

    for _ in range(int(input())):
        print(get_mex_or(int(input())))
except Exception as e:
    pass
