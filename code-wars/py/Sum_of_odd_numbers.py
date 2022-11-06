def row_sum_odd_numbers(n):
    i = ((n - 1) * ((n - 1) + 1) // 2)
    return sum([(2 * o) + 1 for o in range(i, n + i)])


print(row_sum_odd_numbers(1), 1)
print(row_sum_odd_numbers(2), 8)
print(row_sum_odd_numbers(13), 2197)
print(row_sum_odd_numbers(19), 6859)
print(row_sum_odd_numbers(41), 68921)
