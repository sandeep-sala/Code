def tail(n):
    # Base Case
    if n == 0:
        return

    # Operation
    print(n)

    # Recursion
    tail(n-1)


tail(5)
