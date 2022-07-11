def prime_factors(n):
    f = {}
    i = 2
    while n > 1:
        if n % i == 0:
            if i not in f:
                f[i] = 1
            else:
                f[i] += 1
            n = n/i
            i -= 1
        i += 1
    return "".join([ f"({item[0]}**{item[1]})" if item[1] > 1 else f"({item[0]})"  for item in f.items() ])

print(prime_factors(86240))