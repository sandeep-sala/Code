def sum_digits(number):
    s = 0
    number = abs(number)
    while number:
        d = number%10
        s += d
        number = number//10
    return s

print(sum_digits(10), 1)
print(sum_digits(99), 18)
print(sum_digits(-32), 5)