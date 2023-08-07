def mul_by_n(a, b):
    return [i*b for i in a] 

print(mul_by_n([1, 2, 3], 4), [4, 8, 12])
print(mul_by_n([9, 1], 9), [81, 9])
print(mul_by_n([5, 5, 5, 5, 5], 1), [5, 5, 5, 5, 5])
print(mul_by_n([5, 5, 5, 5, 5], 2), [10, 10, 10, 10, 10])
print(mul_by_n([77, 88], 0), [0, 0])
print(mul_by_n([], 1), [])
print(mul_by_n([], 9), [])
