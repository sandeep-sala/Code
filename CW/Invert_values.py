# def invert(lst):
#     return list(map(lambda x: abs(x) if x<0 else -(x) ,lst))

invert = lambda lst : list(map(lambda x: abs(x) if x<0 else -(x) ,lst))

print(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
print(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
print(invert([]), [])