# # this is not fast enough!
# def digit_sum(n):
#     sum = 0
#     while n>9:
#         sum += n%10
#         n //= 10
#     return sum + n

# # this is even worse
# def digit_sum(n):
#     return n if n<9 else n%10 + digit_sum(n//10)


def digit_sum(n):
    return sum(map(int, list(str(n))))



print(digit_sum(0), 0)
print(digit_sum(12345), 15)
print(digit_sum(999), 27)
print(digit_sum(4294967295), 57)
print(digit_sum(2**200), 256)
