
def count_bits(n):
    return bin(n).count("1")




print(count_bits(0), 0)
print(count_bits(4), 1)
print(count_bits(7), 3)
print(count_bits(9), 2)
print(count_bits(10), 2)