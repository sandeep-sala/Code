def divisible_by(numbers, divisor):
    return [ i for i in numbers if i%divisor==0 ]


divisible_by = lambda n, d: [ i for i in n if i%d==0 ]

print(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
print(divisible_by([1,2,3,4,5,6], 3), [3,6])
print(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
print(divisible_by([0], 4), [0])
print(divisible_by([1,3,5], 2), [])
print(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1), [0,1,2,3,4,5,6,7,8,9,10])