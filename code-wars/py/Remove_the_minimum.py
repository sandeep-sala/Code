def remove_smallest(n):
    k = n[::]
    if k:
        k.remove(min(k))
        return k
    return k



print(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])
print(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])
print(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1])
print(remove_smallest([]), [])
