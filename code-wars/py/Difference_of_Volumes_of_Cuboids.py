from functools import reduce as r
def find_difference(a, b):
    s = lambda x,y:x*y
    return abs(r(s,a) - r(s,b))

print(find_difference([3, 2, 5], [1, 4, 4]), 14, "{0} should equal 14".format(find_difference([3, 2, 5], [1, 4, 4])))
print(find_difference([9, 7, 2], [5, 2, 2]), 106, "{0} should equal 106".format(find_difference([9, 7, 2], [5, 2, 2])))