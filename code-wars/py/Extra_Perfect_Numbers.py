def extra_perfect(n):
    return [i for i in range(1,n+1) if i%2!=0]


print(extra_perfect(3), [1,3])
print(extra_perfect(5), [1,3,5])
print(extra_perfect(7), [1,3,5,7])
print(extra_perfect(28), [1,3,5,7,9,11,13,15,17,19,21,23,25,27])
print(extra_perfect(39), [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39])