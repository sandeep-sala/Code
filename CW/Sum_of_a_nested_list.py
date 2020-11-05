def sum_nested(lst):
    sum  = 0
    if type(lst) != list:
        return lst
    else:
        for i in lst:
            sum += sum_nested(i)
    return sum

print(sum_nested([1]), 1)
print(sum_nested([1, 2, 3, 4]), 10)
print(sum_nested(list(range(11))), 55)
print(sum_nested([]), 0)
print(sum_nested([[1], []]), 1)
print(sum_nested([[1, 2, 3, 4]]), 10)
print(sum_nested([[], []]), 0)
print(sum_nested([1, [1], [[1]], [[[1]]]]), 4)
print(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]), 8)
print(sum_nested([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]), 0)