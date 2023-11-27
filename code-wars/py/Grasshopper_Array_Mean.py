def find_average(nums):
    return sum(nums)/len(nums)


print(find_average([1]), 1)
print(find_average([1, 3, 5, 7]), 4)
print(find_average([-1, 3, 5, -7]), 0)
print(find_average([5, 7, 3, 7]), 5.5)
print(find_average([0]), 0)
