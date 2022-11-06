from functools import reduce
def grow(arr):
    return reduce(lambda a,b:a*b,arr)

print(grow([1, 2, 3]), 6)
print(grow([4, 1, 1, 1, 4]), 16)
print(grow([2, 2, 2, 2, 2, 2]), 64)