def positive_sum(arr):
    return sum(filter(lambda x: x > 0, arr))



print(positive_sum([1,2,3,4,5]),15)
print(positive_sum([1,-2,3,4,5]),13)
print(positive_sum([-1,2,3,4,-5]),9)
print(positive_sum([]),0)
print(positive_sum([-1,-2,-3,-4,-5]),0)