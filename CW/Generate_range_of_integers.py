# def generate_range(min, max, step):
#     return [ i for i in range(min,max+1,step) ]

generate_range = lambda min, max, step : [ i for i in range(min,max+1,step) ]

print(generate_range(1, 10, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(generate_range(-10, 1, 1), [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1])
print(generate_range(1, 15, 20), [1])
print(generate_range(1, 7, 2), [1, 3, 5, 7])
print(generate_range(0, 20, 3), [0, 3, 6, 9, 12, 15, 18])