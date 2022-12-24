def calculate_years(principal, interest, tax, desired):
    y = 0
    if principal == desired:
        return 0
    while principal < desired:
        i = principal * interest
        principal = principal + (i - (i * tax))
        y += 1
    return y


print(calculate_years(1000, 0.05, 0.18, 1100), 3)
print(calculate_years(1000, 0.01625, 0.18, 1200), 14)
print(calculate_years(1000, 0.05, 0.18, 1000), 0)
