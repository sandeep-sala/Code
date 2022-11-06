def thirt(n, v=0, b=[1, 10, 9, 12, 3, 4]):
    n = sum(
        [
            n1 * n2
            for n1, n2 in zip(
                [int(x) for x in str(n)][::-1],
                [b[i - 6] if i > 5 else b[i] for i in range(len(str(n)))],
            )
        ]
    )
    if n == v:
        return n
    return thirt(n, n)


print(thirt(1234567), 87)
print(thirt(8529), 79)
print(thirt(85299258), 31)
print(thirt(5634), 57)
print(thirt(1111111111), 71)
print(thirt(987654321), 30)
