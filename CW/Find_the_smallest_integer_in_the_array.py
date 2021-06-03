def find_smallest_int(arr):
    return sorted(arr)[0]

print(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
print(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
print(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)