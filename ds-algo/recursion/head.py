def head(n):
    # Base Case
    if n == 0:
        return

    # Recursion
    head(n-1)

    # Operation
    print(n)


head(5)
