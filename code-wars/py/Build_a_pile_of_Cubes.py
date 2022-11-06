def find_nb(m):
    n = 0
    c = 1
    while m > n:
        n = n + (c**3)
        if n - m == 0:
            return c
        c += 1
    return -1


print(find_nb(4183059834009), 2022)
print(find_nb(24723578342962), -1)
print(find_nb(135440716410000), 4824)
print(find_nb(40539911473216), 3568)
print(find_nb(26825883955641), 3218)
