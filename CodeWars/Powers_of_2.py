def powers_of_two(n):
    return [ 2**i for i in range(n+1) ]



print(powers_of_two(0), [1])
print(powers_of_two(1), [1, 2])
print(powers_of_two(4), [1, 2, 4, 8, 16])