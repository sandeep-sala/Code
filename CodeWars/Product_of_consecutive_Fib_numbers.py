def productFib(prod):
    print(prod)
    tb = [0,1]
    if prod == 1:
        return tb + [True]
    i = 2
    n_p = 0
    while True:
        n_p = tb[-2]*tb[-1]
        if prod == n_p:
            return [tb[-2], tb[-1], True]
        if prod < n_p:
            return [tb[-2], tb[-1], False]
        tb.append(tb[i-1]+tb[i-2])
        i += 1



# print(productFib(4895), [55, 89, True])
# print(productFib(5895), [89, 144, False])
print(productFib(1), [0, 1, True])
print(productFib(1), [1, 1, True])


# [1, 1, False] should equal [0, 1, True]

# [0, 1, True] should equal [1, 1, True]