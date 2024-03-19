def monkey_count(n):
    return [i for i in range(1, n + 1)]


print(monkey_count(5), [1, 2, 3, 4, 5])
print(monkey_count(3), [1, 2, 3])
print(monkey_count(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(
    monkey_count(20),
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
)
