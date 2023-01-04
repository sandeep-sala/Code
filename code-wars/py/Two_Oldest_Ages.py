def two_oldest_ages(ages):
    return sorted(ages)[-2:]


print(two_oldest_ages([1, 5, 87, 45, 8, 8]), [45, 87])
print(two_oldest_ages([6, 5, 83, 5, 3, 18]), [18, 83])
print(two_oldest_ages([10, 1]), [1, 10])